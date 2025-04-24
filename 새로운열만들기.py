import seaborn as sns
import numpy as np
import pandas as pd

df=sns.load_dataset('mpg')

# 기존에 존재하는 데이터를 바탕으로 새로운 열을 만드는 법에 대해 알아보자

df['ratio'] = (df['mpg'] / df['weight']) * 100
df.head()

# 특정 열의 조건을 기반으로 새로운 열을 만들기 , numpy 패키지의 where 함수 활용

num = pd.Series([-2,-1, 1,2])

# True인 지점의 인덱스를 반환
np.where(num>=0)

# 두번째와 세번째인자에 값을 추가하면 조건을 만족하는 부분은 두번째 인자를 그렇지 않은 부분은 세번째 인자를 부여한다.
print(np.where(num>=0, '양수','음수'))

df['horse_power_div'] = np.where(
    df['horsepower'] < 100, '100미만', 
    np.where((df['horsepower'] >= 100) & (df['horsepower'] < 200), '100 이상',
             np.where(df['horsepower'] >= 200, '200이상','기타')))

print(df.head(8))

