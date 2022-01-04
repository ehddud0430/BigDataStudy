#11.데이터정렬
import pandas as pd
df=pd.read_excel('score.xlsx', index_col='지원번호')
df
#        이름    학교    키  국어 영어 수학 과학 사회  SW특기    
# 지원번호
# 1번    채치수  북산고  197   90   85  100  95  85      Python
# 2번    정대만  북산고  184   40   35   50  55  25        Java
# 3번    송태섭  북산고  168   80   75   70  80  75  Javascript
# 4번    서태웅  북산고  187   40   60   70  75  80         NaN
# 5번    강백호  북산고  188   15   20   10  35  10         NaN
# 6번    변덕규  능남고  202   80  100   95  85  80           C
# 7번    황태산  능남고  188   55   65   45  40  35      PYTHON
# 8번    윤대협  능남고  190  100   85   90  95  95          C#
df.sort_values('키') #키순으로 오름차순 정렬
df.sort_values('키', ascending=False) #내림차순

df.sort_values(['수학','영어'], ascending=False) #수학(1순위), 영어(2순위)기준으로 내림차순
df.sort_values(['수학','영어'], ascending=[True,False]) #수학점수는 오름차순, 영어점수는 내림차순


