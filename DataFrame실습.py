import pandas as pd


dict_data = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}
df = pd.DataFrame(dict_data)

# print(df)

df2 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
# print(df2)

df3 = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]], index=['idx1','idx2','idx3'],columns=['col1','col2','col3'])
# print(df3)

df3.index = ['행1','행2','행3']
df3.columns = ['열1','열2','열3']
print(df3)

print(df3.loc['행1','열2'])
print(df3.loc[['행1','행3'],['열2','열3']])
