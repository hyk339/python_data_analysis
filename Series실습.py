import pandas as pd

dict_data = {'a':1, 'b':2, 'c':3}
series = pd.Series(dict_data)

print(series)
# print(series.index)
# print(series.values)

list_data = ['a', 'b', 'c']
series_2 = pd.Series(list_data)

print(series_2)