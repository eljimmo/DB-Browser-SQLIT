import numpy as np
import pandas as pd

df = pd.DataFrame([['1990', 'a', 5, 4, 7, 2], ['1991', 'c', 10, 1, 2, 0], ['1992', 'd', 2, 1, 4, 12], ['1993', 'a', 5, 8, 11, 6]], columns=('Date', 'best', 'a', 'b', 'c', 'd'))
df


#Given equal-length arrays of row and column labels, 
# #return an array of the values corresponding to each (row, col) pair.

#result = [df.get_value(row, col)
#          for row, col in zip(row_labels, col_labels)]

#DataFrame.lookup(self, row_labels, col_labels)


#https://www.w3resource.com/pandas/dataframe/dataframe-lookup.php


df['value'] = df.lookup(df.index, df['best'])
print(df)

