import argparse
import base64
import http.client
import mimetypes
import os
import subprocess
import sys
import tempfile
import uuid
import zipfile
from pathlib import Path
from urllib.parse import urlparse


def run_build(repo_root: Path) -> int:
    try:
        npm_cmd = "npm.cmd" if os.name == "nt" else "npm"
        result = subprocess.run(
            [npm_cmd, "run", "build"],
            cwd=str(repo_root),
            check=False,
        )
        return result.returncode
    except FileNotFoundError:
        print("npm not found. Install Node.js and npm first.", file=sys.stderr)
        return 1


def collect_doc_files(root: Path) -> set[str]:
    files = set()
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".mdx"}:
            files.add(path.relative_to(root).as_posix())
    return files


def validate_i18n(repo_root: Path) -> int:
    docs_root = repo_root / "docs"
    i18n_root = repo_root / "i18n"
    if not docs_root.exists() or not i18n_root.exists():
        return 0

    source_files = collect_doc_files(docs_root)
    language_dirs = [
        path
        for path in i18n_root.iterdir()
        if path.is_dir() and (path / "docusaurus-plugin-content-docs" / "current").exists()
    ]

    for lang_dir in language_dirs:
        lang_docs = lang_dir / "docusaurus-plugin-content-docs" / "current"
        translated_files = collect_doc_files(lang_docs)
        missing = sorted(source_files - translated_files)
        extra = sorted(translated_files - source_files)
        if missing or extra:
            print(f"I18n mismatch in language '{lang_dir.name}':", file=sys.stderr)
            if missing:
                print("  Missing files:", file=sys.stderr)
                for item in missing:
                    print(f"    - {item}", file=sys.stderr)
            if extra:
                print("  Extra files:", file=sys.stderr)
                for item in extra:
                    print(f"    - {item}", file=sys.stderr)
            return 1

    return 0


def zip_directory(source_dir: Path) -> Path:
    temp_dir = Path(tempfile.mkdtemp(prefix="docusaurus-build-"))
    zip_path = temp_dir / "build.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        for file_path in source_dir.rglob("*"):
            if file_path.is_file():
                zipf.write(file_path, file_path.relative_to(source_dir))
    return zip_path


def build_multipart(fields: dict, file_field: str, file_path: Path) -> tuple[bytes, str]:
    boundary = f"----DocUpload{uuid.uuid4().hex}"
    lines: list[bytes] = []

    for key, value in fields.items():
        lines.append(f"--{boundary}".encode())
        lines.append(f'Content-Disposition: form-data; name="{key}"'.encode())
        lines.append(b"")
        lines.append(str(value).encode())

    filename = file_path.name
    content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    lines.append(f"--{boundary}".encode())
    lines.append(
        f'Content-Disposition: form-data; name="{file_field}"; filename="{filename}"'.encode()
    )
    lines.append(f"Content-Type: {content_type}".encode())
    lines.append(b"")
    lines.append(file_path.read_bytes())
    lines.append(f"--{boundary}--".encode())
    lines.append(b"")

    body = b"\r\n".join(lines)
    return body, boundary


def upload_build(upload_url: str, secret: str, zip_path: Path) -> int:
    parsed = urlparse(upload_url)
    if parsed.scheme not in {"http", "https"}:
        print("Upload URL must start with http:// or https://", file=sys.stderr)
        return 1

    secret_b64 = base64.b64encode(secret.encode("utf-8")).decode("ascii")
    body, boundary = build_multipart({"secret_b64": secret_b64}, "build", zip_path)
    headers = {
        "Content-Type": f"multipart/form-data; boundary={boundary}",
        "Content-Length": str(len(body)),
        "User-Agent": "itsmagic-docs-uploader/1.0",
    }

    conn_class = http.client.HTTPSConnection if parsed.scheme == "https" else http.client.HTTPConnection
    conn = conn_class(parsed.netloc)
    try:
        path = parsed.path or "/"
        if parsed.query:
            path = f"{path}?{parsed.query}"
        conn.request("POST", path, body=body, headers=headers)
        response = conn.getresponse()
        response_body = response.read().decode("utf-8", errors="replace")
        if response.status >= 400:
            print(f"Upload failed: {response.status} {response.reason}", file=sys.stderr)
            print(response_body, file=sys.stderr)
            return 1
        print(response_body)
        return 0
    finally:
        conn.close()


DEFAULT_UPLOAD_URL = "https://itsmagic.com.br/docdeployer/updateDoc.php"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build Docusaurus and upload the build.")
    parser.add_argument("--url", help="Upload endpoint URL (PHP).")
    parser.add_argument("--secret", help="Upload secret.")
    parser.add_argument("--secret-file", help="Path to a file containing the upload secret.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    build_dir = repo_root / "build"

    secret = None
    if args.secret_file:
        try:
            secret = Path(args.secret_file).read_text(encoding="utf-8").rstrip("\r\n")
        except FileNotFoundError:
            print(f"Secret file not found: {args.secret_file}", file=sys.stderr)
            return 1
    if secret is None:
        secret = args.secret or os.getenv("DOC_UPLOAD_SECRET")
    upload_url = args.url or os.getenv("DOC_UPLOAD_URL") or DEFAULT_UPLOAD_URL

    if not secret:
        print("Upload secret missing. Use --secret or DOC_UPLOAD_SECRET.", file=sys.stderr)
        return 1

    i18n_code = validate_i18n(repo_root)
    if i18n_code != 0:
        return i18n_code

    build_code = run_build(repo_root)
    if build_code != 0:
        return build_code

    if not build_dir.exists():
        print(f"Build output not found: {build_dir}", file=sys.stderr)
        return 1

    zip_path = zip_directory(build_dir)
    return upload_build(upload_url, secret, zip_path)


if __name__ == "__main__":
    raise SystemExit(main())
