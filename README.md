# ConsoleDEW
Method for Determination of Epidemiological Waves Based on the non-linear Richards Growth Function

# How to use:
This project was developed with Python.
To use the system, perform:
1) Download the files
2) Preparation of the Database to be analyzed:
The database must be a CSV format file with two columns. The first column must contain the dates of the epidemiological data and the second column must contain the accumulated values of the recorded observations. the first line of the file must contain: ["date, totalcases"]
3) make sure that the database is properly stored in the subdirectory: Files --> Dataset
-----
Once you have the file to be analyzed in its proper location, you must listen to the function: PerformBestParametersAnalysis. This function will generate a file containing the best parameters for the data that will be analyzed in the subdirectory: Files -->BestParameters
-----
Running DEW:
1) once you have the files in your subdirectories, run the runHermes() function.
