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

#### 2. Performing deeplearnig:

```bash
PerformBestParametersAnalysis.ipynb
```
This function will generate a file containing the best parameters for the data that will be analyzed in the subdirectory: 

- Files
  - BestParameters

#### 3. Running the DEW script locally:

```bash
PerformDEW.ipynb
```
