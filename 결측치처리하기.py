import seaborn as sns

## 3.5 결측치 처리하기

df = sns.load_dataset('titanic')

#isnull(): 결측치면 True, 유효한 데이터면 False를 반환

df.head().isnull()

#notnull(): 유효한 데이터면 True, 결측치면 False를 반환

## ------------------ 결측치 삭제하기 --------------------------
 
# dropna() 메서드는 결측치가 있을 경우 해당 행을 모두 삭제
df.dropna()

# dropna() 메서드 내에 subset을 입력하면 해당 열 중에서 결측치가 있는 경우 행을 삭제, axis = 0은 행 방향으로 동작, 1은 열 방향으로 동작

df.dropna(axis=1)

# 결측치가 300개 이상 갖는 열을 삭제하겠다는 의미
df.dropna(axis=1, thresh=300)

## ------------------ 결측치 대체하기 --------------------------

df_2 = df.copy()
df_2.head(6)

mean_age = df_2['age'].mean()

# fillna() 내에 인자를 입력하면 결측치를 해당 값을 대체한다. inplace=True를 입력하면 원본객체를 변경
df_2['age'].fillna(mean_age,inplace=True)

#print(df_2['age'].head(6))


# 숫자가 아닌 문자로 변경할때
df_2['embark_town'].fillna('Southampton', inplace=True)

# 결측치를 직전 행의 값으로 바꾸기. ffill은 위의 행 중 결측치가 나타나기 전의 값으로 바꿔줌. bfill은 아래의 행중 결측치가 아닌 첫번째 값으로 바꿔줌
df_2['deck_ffill'] = df_2['deck'].fillna(method='ffill')
df_2['deck_bfill'] = df_2['deck'].fillna(method='bfill')

print(df_2[['deck', 'deck_ffill', 'deck_bfill']].head(12))



