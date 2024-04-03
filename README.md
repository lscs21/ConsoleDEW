# DEW
This project aims to provide analyzes of multiple epidemiological waves through the use of a method developed in the PIMAT Research Group at the Universidade do Estado da Bahia (UNEB), Brazil.

It contemplates a deep learning method to find the best parameters for determining the epidemiological waves of a pandemic, using the Richards growth function as the main engine for data modeling.

With a correction factor greater than 99.5%, the method is efficient and effective for the healthcare community, allowing precise analyzes of wave overlap as well as their start, peak and end dates.

# Preliminary:

#### 1. Download and Install Python

```bash
https://www.python.org/downloads/
```


##### Windows:

- Visit the [official Python website](https://www.python.org/downloads/).
- Download the installer for Windows.
- Run the installer and follow the instructions.
- Make sure to check the option "Add Python to PATH" during installation.

##### macOS:

- Python comes pre-installed by default on macOS. However, you may want to install a newer version. You can do this through Homebrew or by downloading the installer from the [official website](https://www.python.org/downloads/).

##### Linux:

- Most Linux distributions already include Python. You can check by typing `python3 --version` in the terminal. If it's not installed, you can install it using your distribution's package manager. For example, on Ubuntu, you can use `sudo apt-get install python3`.

#### 2. Install a Text Editor or IDE:

- You can use any text editor to write Python code, such as Visual Studio Code, Atom, Sublime Text, or your operating system's default text editor.
- Additionally, there are Python-specific IDEs such as PyCharm, Spyder, or IDLE.

#### 3. Verify the Installation:

- After installation, you can verify if Python was installed correctly by typing `python --version` or `python3 --version` in the terminal or command prompt, depending on your operating system.
- To check if pip (Python package manager) was installed correctly, type `pip --version` or `pip3 --version`.

---

# DEW Environment:



## How to Setup

#### Clone the repository

```bash
git clone https://github.com/lscs21/dew.git
```

#### Then move to the project local directory

```bash
cd DEW
```

#### Download the project submodules

```bash
git submodule update --init
```

### Project file structure 

- DEW/
  - covid.py
  - curve_functions.py
  - data_process.py
  - DEW.py
  - plot_function.py
  - System_Functions.py
  - PerformBestParametersAnalysis.ipynb
  - PerformDEW.ipynb
  - Files/
    - BestParameters/
    - Dataset/

### How to Start

#### 1. Preparation of the Database to be analyzed:

```bash
The database must be a CSV format file with two columns.
The first column must contain the dates of the epidemiological data
The second column must contain the accumulated values of the recorded observations.
The first line of the file must contain the strings: ["date, totalcases"]
Make sure that the database is properly stored in the subdirectory: Files --> Dataset
```
##### example file 

```bash
date, totalcases
3/1/2020,1
3/2/2020,2
3/3/2020,2
3/4/2020,3
3/5/2020,8
3/6/2020,13
3/7/2020,19
3/8/2020,25
3/9/2020,25
3/10/2020,34
3/11/2020,52
3/12/2020,77
3/13/2020,151
3/14/2020,151
3/15/2020,200
3/16/2020,234
3/17/2020,347
3/18/2020,531
3/19/2020,643
....
```

##### File name:
There is no rule for file naming. However, we recommend that it be a short, easy-to-understand name.

Example: Covid_TotalCases_Brazil.csv

**Attention**: This same file name must be used, in its full form, with extension (.csv), within the PerformBestParametersAnalysis() function as well as in the runDEW() function


#### 2. Performing deeplearnig:

For the system to function, it is mandatory that the process of discovering the best parameters is carried out.

This process involves iterating regressions with the Richards function to determine the best parameters.

The parameters that can be changed are:

###### DataSetFileName........: Complete name of dataser file, with extension (.csv). Example: "Covid_TotalCases_Brazil.csv"

###### MaxChunckSize..........: Maximum sife for chuck data

###### MaxWaveOffset..........: Maximum sife for waves offset

###### MaxMovingAverageIndex..: Maximum sife for Moving Average Index 

run:

```bash
PerformBestParametersAnalysis.ipynb
```

This function will generate a file containing the best parameters for the data that will be analyzed in the subdirectory: 

- Files
  - BestParameters

#### 3. Running the DEW script:

This step will check the file produced in the previous step and select the best possible parameters for data analysis.

The parameters that can be changed are:

###### FileName........: Complete name of dataser file, with extension (.csv). Example: "Covid_TotalCases_Brazil.csv"
###### GeneralPredictiveCapacityInDays.: Future data prediction target

```bash
PerformDEW.ipynb
```
