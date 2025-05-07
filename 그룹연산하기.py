import seaborn as sns

df  = sns.load_dataset('penguins')

# 그룹 나누기

df_groupby = df.groupby(['species'])

df_groupby.head(2)

#for key, group in df_groupby:
#    print(key)
#    print(group.head(2))

# 그룹별 연산하기

# df_groupby.mean()

# print(df.groupby(['species','sex']).mean())

#def min_max(x):
#    return x.max() - x.min()

#print(df.groupby(['species'])['bill_length_mm'].agg(min_max))

df  = sns.load_dataset('penguins')
print(df.groupby(['species']).agg(['max','min']))




