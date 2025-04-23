import seaborn as sns

## 3.6 인덱스 다루기

df = sns.load_dataset('mpg')

# 인덱스를 확인해보면 0,1,2,3로 되어있다.
df.head()

# name열을 인덱스로 설정하자.
df.set_index('name', inplace=True)
df.head()


# 인덱스를 순서대로 정렬해보자. 인덱스 정렬에는 sort_index()메서드가 사용된다.
df.sort_index(inplace=True)
df.head()

# 내림차순으로 정렬하고 싶은경우 ascending = False
df.sort_index(inplace=True, ascending=False)
df.head()

# 인덱스 재설정에는 reset_index() 메서드를 사용한다.
df.reset_index(inplace=True)
print(df.head())