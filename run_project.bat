@echo off
echo Movie Recommendation System Setup
echo ================================

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo Virtual environment created successfully.
) else (
    echo Virtual environment already exists.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install requirements
echo Installing requirements...
pip install -r requirements.txt

REM Run the main application
echo.
echo Starting Movie Recommendation System...
echo.
python main.py

REM Keep the window open after the program finishes
echo.
echo Program finished. Press any key to exit...
pause > nul
