#6.데이터 선택(기본)
import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')
df

##column 선택(label)
df['키'] # '키' 데이터만 출력
df[['이름', '학교']] #'이름' 과 '학교 데이터 출력

##column 선택(정수 index)
df.columns[2] #키
df.columns[5] #수학

df[df.columns[2]] #'키' 데이터를 col의 index를 통해서 출력
df[df.columns[-1]] #'SW특기' 데이터를 col의 index를 통해서 출력

##슬라이싱
df['영어'][0:5] #'영어' 데이터중에서 index 0~4까지 데이터 출력
df[['이름','영어']][:3] #index 0~2에 해당하는 학생들의 이름,영어 점수를 출력

df[:3]



