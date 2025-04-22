import seaborn as sns

# 데이터의 맨위와 아래중 일부를 확인할때, head() tail() 메서드 사용

df = sns.load_dataset('titanic')

# 데이터의 맨위 일부 확인 head()
df.head(10)

# 데이터의 아래 일부 확인 tail()
df.tail(5)

# 데이터프레임의 크기 확인
df.shape

# 데이터프레임 기본 정보
#df.info()

# 한 개 열의 고윳값 개수 구하기 value_counts()
df['sex'].value_counts()

# 여러 열의 고윳값 개수 구하기 value_counts()
df[['sex','survived']].value_counts()

# 비중으로 보기
df[['sex','survived']].value_counts(normalize=True).sort_index()

# 산술평균은 mean() 
df['survived'].mean()

# 여러개의 열 리스트형태로 입력, 동시에 평균구하기
print(df[['survived','age']].mean())

# 해당 열의 최소값, 최대값, 평균값
df['fare'].min()
df['fare'].max()
df['fare'].mean()

# 중위수
df['fare'].median()

# 이외에도 통계값을 계산할수 있는 다양한 메서드가 존재한다.
