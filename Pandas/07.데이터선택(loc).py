#7.데이터 선택(loc/location(위치))
#이름을 이용하여 원하는 row에서 원하는 col 선택
import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')
df

df.loc['1번','국어']
df.loc[['1번','3번'],'수학']
df.loc[['1번','3번'],['수학','국어']]

##슬라이싱 활용
df.loc['1번':'5번','국어':'수학'] #주의사항 : 일반적인 슬라이싱과 다르게 loc에서의 슬라이싱은 x : y 일경우 y까지 포함하여 데이터를 출력한다.




