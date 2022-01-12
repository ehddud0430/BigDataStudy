#14.그룹화
 #동일한 값을 가진 것들끼리 합쳐서 통계 또는 평균값을 계산하기 위해 사용
import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')
df

df.groupby('학교').get_group('북산고')

df.groupby('학교').mean() #계산 가능한 데이터들의 평균값
df.groupby('학교').size() #각 그룹의 크기

df.groupby('학교').mean()[['키','국어']]

df['학년']=[3,3,2,1,1,3,2,3] #학년 col추가

df.groupby(['학교','학년']).mean() #학교,학년 별 평균 데이터
df.groupby('학년').mean().sort_values('키') #학년별 평균키를 기준으로 오름차순 정렬
df.groupby('학년').mean().sort_values('키',ascending=False) #학년별 평균키를 기준으로 내림차순 정렬

school = df.groupby('학교')
school['학년'].value_counts() #학교로 그룹화를 한 뒤에 학년별 학생 수를 가져옴

school['학년'].value_counts().loc['북산고'] #학교로 그룹화를 한 뒤에 북산고의 학년별 학생 수를 가져옴
school['학년'].value_counts(normalize=True).loc['북산고'] #학년별 학생수를 퍼센트로 비교하여 가져옴








