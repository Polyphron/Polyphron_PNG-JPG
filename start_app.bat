@echo off

:: Check if virtual environment exists
if not exist "env\Scripts\activate.bat" (
    echo Virtual environment does not exist. Please run setup.bat to create it.
    exit /b 1
)

:: Activating the virtual environment
call env\Scripts\activate.bat

:: Starting the application
python main.py
if %errorlevel% neq 0 (
    echo Failed to start the application. Please check the logs for more details.
    exit /b %errorlevel%
)

echo Application started successfully.
pause