@echo off

:: Check for Python 3.10.6 and exit if not found
python --version | find "3.10.6" > nul
if errorlevel 1 (
    echo Python 3.10.6 is required to run this setup.
    echo Please install Python 3.10.6 and try again.
    exit /b 1
)

:: Creating a virtual environment
echo Creating a virtual environment...
python -m venv env
if errorlevel 1 (
    echo Failed to create a virtual environment.
    exit /b 1
) else (
    echo Virtual environment created successfully.
)

:: Activating the virtual environment
echo Activating the virtual environment...
call env\Scripts\activate.bat
if errorlevel 1 (
    echo Failed to activate the virtual environment.
    exit /b 1
) else (
    echo Virtual environment activated successfully.
)

:: Installing Pillow
echo Installing Pillow...
pip install Pillow
if errorlevel 1 (
    echo Failed to install Pillow.
    exit /b 1
) else (
    echo Pillow installed successfully.
)

echo Setup completed successfully. You can now run the application using start_app.bat