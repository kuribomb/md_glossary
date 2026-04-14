@echo off
echo Setting up Python virtual environment...
py -m venv .venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment. Is Python 3.12 installed?
    exit /b 1
)

echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM --- PROXY settings (uncomment and edit if you are behind a proxy) ---
REM set HTTP_PROXY=http://proxy.example.com:8080
REM set HTTPS_PROXY=http://proxy.example.com:8080
REM set NO_PROXY=localhost,127.0.0.1

echo Upgrading pip...
.venv\Scripts\python.exe -m pip install --upgrade pip
if errorlevel 1 (
    echo ERROR: Failed to upgrade pip.
    exit /b 1
)

echo Installing dev dependencies...
.venv\Scripts\python.exe -m pip install -e ".[dev]"
if errorlevel 1 (
    echo ERROR: Failed to install dependencies.
    exit /b 1
)

echo.
echo Setup complete!
echo To activate the venv in a new terminal, run:
echo   .venv\Scripts\activate.bat
