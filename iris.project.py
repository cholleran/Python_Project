# pandas is a package in Python which is used for data analysis.
# The code on line 3 imports pandas which enables use of the functions in the pandas library.
# The code on line 7 asks pandas to read the file and create a dataframe.
# The dataframe is a structured grid/array which prepares the data for analysis.
# The pandas library is already installed with Anaconda.

import pandas as pd

# Adding column names: https://chrisalbon.com/python/data_wrangling/pandas_dataframe_importing_csv/
dataframe = pd.read_csv("C:\\Users\MyComputer\Desktop\projects\Data\iris.csv", names=['Sl_Length', 'Sl_width', 'Pl_Length', 'Pl Width', 'Class'])

# .to_string() formats the data for printing: https://stackoverflow.com/questions/19124601/is-there-a-way-to-pretty-print-the-entire-pandas-series-dataframe
print(dataframe.to_string())
