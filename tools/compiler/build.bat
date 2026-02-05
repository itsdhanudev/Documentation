@echo off
setlocal

set "SCRIPT_DIR=%~dp0"
set "SECRET_FILE=%SCRIPT_DIR%..\secrets\docsecret.txt"

if not exist "%SECRET_FILE%" (
  echo Secret file not found: %SECRET_FILE%
  exit /b 1
)

set "DOC_UPLOAD_URL_ARG=%~1"
if not "%DOC_UPLOAD_URL_ARG%"=="" set "DOC_UPLOAD_URL=%DOC_UPLOAD_URL_ARG%"

if not "%DOC_UPLOAD_URL%"=="" (
  python "%SCRIPT_DIR%build.py" --url "%DOC_UPLOAD_URL%" --secret-file "%SECRET_FILE%"
) else (
  python "%SCRIPT_DIR%build.py" --secret-file "%SECRET_FILE%"
)
endlocal
