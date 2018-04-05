# pandas is a package in Python which is used for data analysis.
# The code on line 3 imports pandas which enables use of the functions in the pandas library.
# The code on line 7 asks pandas to read the file and create a dataframe.
# The dataframe is a structured grid/array which prepares the data for analysis.
# The pandas library is already installed with Anaconda.

import pandas as pd

dataframe = pd.read_csv("C:\\Users\MyComputer\Desktop\projects\Data\iris.csv")

print(dataframe)