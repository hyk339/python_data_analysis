import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('penguins')

# 산점도
## plt.scatter(df['flipper_length_mm'],df['body_mass_g'])
## plt.show()

df_group = df.groupby('species')['body_mass_g'].mean().reset_index()

# 막대그래프
## plt.bar(x=df_group['species'], height=df_group['body_mass_g'])
## plt.show()

# 히스토그램
plt.rc('font', family='Malgun Gothic')
plt.hist(df['body_mass_g'], bins=30)
plt.xlabel('Body Mass')
plt.ylabel('Count')
plt.title('펭귄의 몸무게 분포')
## plt.show()

df_unrate = pd.read_csv(
    'https://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv'
)

df_unrate.head()

df_unrate['DATE'] = pd.to_datetime(df_unrate['DATE'])

# 선그래프
plt.plot(df_unrate['DATE'], df_unrate['VALUE'])
plt.show()


