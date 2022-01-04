#9.데이터선택(조건)
import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')
df

df['키'] >= 185

filt = (df['키'] >= 185)
df[filt]
df[~filt] #반대로 뒤집는다

df.loc[filt, '수학'] #키가 185이상인 학생들의 수학점수
df.loc[filt, ['이름','영어','수학']]

##다양한 조건
###&(그리고)
df.loc[(df['키']>=185) & (df['학교']=='북산고')]


### |(또는)
df.loc[(df['키'] < 170)|(df['키'] > 200)] #키가 170보다 작거나, 200보다 큰 학생들의 데이터

##str함수
filt = df['이름'].str.startswith('송') #송으로 시작하는 사람
df[filt]

filt = df['이름'].str.contains('태')
df[filt] #이름에 '태'가들어간 사람
df[~filt] #이름에 '태'가들어간 사람 제외

langs = ['Python','Java']
filt = df['SW특기'].isin(langs) #sw 특기가 파이썬이나 자바인 사람
df[filt]
langs = ['python','java']
filt = df['SW특기'].str.lower().isin(langs)
df[filt]

filt = df['SW특기'].str.contains('Java',na=False)
df[filt]  