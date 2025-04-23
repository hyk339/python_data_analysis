import seaborn as sns

## 3.7 필터링
## 불리언 인덱싱과 isin() 메서드가 사용된다.

## 3.7.1 불리언 인덱싱
## 시리즈 객체에 조건을 입력하면 각 원소에 대해 참 또는 거짓을 판별하여 True/False로 이루어진 시리즈가 반환된다.
## 그 후 참에 해당하는 데이터만 선택하면 결과적으로 조건을 만족하는 데이터만 추출할 수 있다.

df=sns.load_dataset('mpg')
df.tail(10)

# unique() 메서드는 고유한 값을 반환
df['cylinders'].unique()


# 실린더 열이 4인 조건을 의미. 4인 원소는 True 반환, 그렇지 않으면 False
filter_bool = (df['cylinders'] == 4)
filter_bool.head()

# 행 인덱스에 불리언 시리즈를 입력하면 해당 조건을 만족하는 행만 선택된다.
df.loc[filter_bool,]

filter_bool_2 = (df['cylinders'] == 4) & (df['horsepower'] >= 100)
#print(filter_bool_2)

print(df.loc[filter_bool_2,['cylinders','horsepower','name']])








