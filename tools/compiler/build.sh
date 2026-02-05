#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
SECRET_FILE="${REPO_ROOT}/tools/secrets/docsecret.txt"

if [[ ! -f "${SECRET_FILE}" ]]; then
  echo "Secret file not found: ${SECRET_FILE}" >&2
  exit 1
fi

DOC_UPLOAD_URL="${1:-${DOC_UPLOAD_URL:-}}"

if [[ -n "${DOC_UPLOAD_URL}" ]]; then
  python "${SCRIPT_DIR}/build.py" --url "${DOC_UPLOAD_URL}" --secret-file "${SECRET_FILE}"
else
  python "${SCRIPT_DIR}/build.py" --secret-file "${SECRET_FILE}"
fi
