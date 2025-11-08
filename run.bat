@echo off
ECHO Running Python Project...

REM Get the directory of this .bat file
SET "BATCH_DIR=%~dp0"

REM Activate the virtual environment using the Windows path
CALL "%BATCH_DIR%.venv\Scripts\activate.bat"

ECHO Virtual environment activated.
ECHO Installing dependencies from requirements.txt...

REM Install requirements. 
REM If packages are already installed, pip will report "Requirement already satisfied".
pip install -r "%BATCH_DIR%requirements.txt"

ECHO Dependencies are up to date. Running script...
ECHO -------------------------------------------------

REM Run the python script. 
REM We use "python" as this is the command used by the virtual env on Windows.
python "%BATCH_DIR%src\series.py"

ECHO -------------------------------------------------
ECHO Script execution finished.
PAUSE

