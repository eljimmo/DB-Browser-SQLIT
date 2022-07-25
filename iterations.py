###DataFrame.iteritems(self)


import numpy as np
import pandas as pd

df = pd.DataFrame({'species': ['mammal', 'mammal', 'fish'],
                   'population': [3948, 4000, 6000]},
                  index=['tiger', 'fox', 'shark'])



for label, content in df.items():
    print('label:', label)
    print('content:', content, sep='\n')

print(df)

#https://www.w3resource.com/pandas/dataframe/dataframe-iteritems.php
