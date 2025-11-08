# My DataFrame

## Project Description
In this project I implement the Pandas DataFrame, I started implementing the pandas series since the dataframe is built using the pandas Series, the project contains unittests and when finished I will use it in a machine learning workflow.

## Installation
1) Navigate to the root of the project directory

2) Run this command in your terminal if youre on linux to create a python virtual environment:
```bash
python3 -m venv .venv
```

3) Now run this command in order to activate the virtual environment: 
```bash
source .venv/bin/activate   # On linux
source .venv/Scripts/activate   # On windows
```

4) Now run this command to install all the dependancies:
```bash
pip install -r requirements.txt
```

## Running the Project
To run the project you can run the series.py file which displays the output for the current supported inputs, it also displays accessing elements via loc with labels, iloc with integer indexing and displays the slicing functionality implemented.

1) While you're in the root directory of the project you can run the series.py with: 
```bash
python3 src/series.py
```

2) You can also run the unit tests I made by running this command in the terminal in the root directory of the project: 
```bash
pytest
```

3) You can also double click the .bat file that is located in the root directory of the project which will install libraries and run the series.py script.