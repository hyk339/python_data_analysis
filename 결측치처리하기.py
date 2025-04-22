import seaborn as sns

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

