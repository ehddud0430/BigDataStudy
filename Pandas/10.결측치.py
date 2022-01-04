#결측치
#비어 있는 데이터
import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')
df
#        이름   학교    키   국어   영어   수학  과학  사회        SW특기    
# 지원번호
# 1번    채치수  북산고  197   90   85  100  95  85      Python
# 2번    정대만  북산고  184   40   35   50  55  25        Java
# 3번    송태섭  북산고  168   80   75   70  80  75  Javascript
# 4번    서태웅  북산고  187   40   60   70  75  80         NaN
# 5번    강백호  북산고  188   15   20   10  35  10         NaN
# 6번    변덕규  능남고  202   80  100   95  85  80           C
# 7번    황태산  능남고  188   55   65   45  40  35      PYTHON
# 8번    윤대협  능남고  190  100   85   90  95  95          C#

df.fillna('없음') #na값을 채움
import numpy as np
df['학교'] = np.nan #학교 데이터 전체를 nan 으로 채움
df.fillna('없음', inplace=True)
df

df['SW특기'].fillna('확인중', inplace=True)
df

##데이터 제외하기(dropna)
df.dropna(inplace=True)
df

##axis : index or columns
##how : any or all
### any : nan이 하나라도 있는경우 삭제
### all : 반드시 전부 nan일 경우 삭제
df.dropna(axis='columns', how='any') #column삭제
df.dropna(axis='index', how='any') #index삭제


