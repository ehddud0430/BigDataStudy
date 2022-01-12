import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')
df
#8.데이터선택(iloc/integerlocation:정수위치)
#위치를 이용하여 원하는 row 에서 원하는 col선택

df.iloc[0] #1번 채치수 학생의 데이터
##슬라이싱
df.iloc[0:5] #0~4 index값의 데이터 출력
df

df.iloc[3,2] #서태웅의 키
df.iloc[6,8] #황태산의 sw특기

df.iloc[[0,1],2] #채치수와 정재만의 키

#슬라이싱
df.iloc[0:5,3:8] #1~5번 학생의 국,영,수,과,사 점수


