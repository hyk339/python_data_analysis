import pandas as pd 

## ---------csv 파일 불러오는 법---------

# read_csv() 함수 내에 파일 경로(파일명)을 입력하면 CSV 파일을 불러온 후 데이터프레임으로 변환
data_csv = pd.read_csv('https://raw.githubusercontent.com/hyunyulhenry/quant_py/main/kospi.csv')

# to_csv() 메서드로 csv 파일로 저장할 수 있다.
data_csv.to_csv('data.csv')









 