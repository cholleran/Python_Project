# pandas is a package in Python which is used for data analysis.
# The code on line 3 imports pandas which enables use of the functions in the pandas library.
# The code on line 7 asks pandas to read the file and create a dataframe.
# The dataframe is a structured grid/array which prepares the data for analysis.
# The pandas library is already installed with Anaconda.
# Imported numpy and matplotlib which are the main packages for visualising data in Python.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Adding column names: https://chrisalbon.com/python/data_wrangling/pandas_dataframe_importing_csv/
dataframe = pd.read_csv("C:\\Users\MyComputer\Desktop\projects\Data\iris.csv", names=['Sl_Length', 'Sl_width', 'Pl_Length', 'Pl Width', 'Class'])

# .to_string() formats the data for printing: https://stackoverflow.com/questions/19124601/is-there-a-way-to-pretty-print-the-entire-pandas-series-dataframe
print(dataframe.to_string())

print(dataframe.describe())

#The below line of code creates a new object containing the data organized by species.https://chrisalbon.com/python/data_wrangling/pandas_apply_operations_to_groups/
#It also produces a histogram of each variable for each species. https://machinelearningmastery.com/quick-and-dirty-data-analysis-with-pandas/
grouped = dataframe.groupby("Class").hist()

print(grouped)

