#13.함수적용
import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')
df

df['학교']=df['학교']+'등학교'
df 
##데이터 함수 적용(apply)
def add_cm(height):
    return str(height) + 'cm'
#정수'키'를 문자열로바꾸고 뒤에 cm을 추가해주는 함수

df['키'] = df['키'].apply(add_cm)
df

def capitalize(lang):
    if pd.notnull(lang):
        return lang.capitalize()
    return lang
#만일lang이 null(nan)이 아니면, lang을 첫글자를 대문자,나머지를 소문자로 변환해주는 함수
df['SW특기']=df['SW특기'].apply(capitalize)
df

##
df['SW특기']=df['SW특기'].str.capitalize()
df

