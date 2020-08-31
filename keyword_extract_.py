import pandas as pd
import numpy as np
import csv
#주소 각자 폴더에 맞게 고치시면 됩니당

list_ = ['의약품','의약','CT','X-RAY','암','담배','금연','방사선','응급', '의원' ,'의료기관', '의료복지', '보건소','의료기','화장품','치과','고혈압'
         ,'성인병','구급','한의학', '의료용어', '진단용어', '보건소', '약국', '의료','약','건강', '담배','진료기관','접종','임신','메디컬스트리트'
         ,'병원','공공보건','의원','검사','당뇨', '보건','혈액','병의원','검진','건강보험','급여비','비급여','한의원','입원','방역','감염','인플루엔자'
         ,'조제','코로나','검역','유증상자','소독','황열','콜레라','오염지역','오염국가','뎅기','혈소판','증후군','바이러스','선별진료소','보건복지부','식중독'
         ,'참진드기','메디칼','메디컬','퇴원','의사','환자','병명','한약','배아연구','생명윤리','유병율','생존율','코호트','질병','수술','약제','보건','엑스레이'
         ,'건강기능식품','주사','병','검진','약방','산모','산후조리원','반려견','반려동물','고양이','개','유기동물','MRI','투여','병용','처방'
         ,'병리','검사','소독','보건위생','재활','산재','약사','건강증진센터','보건지소','의용공학']



df = pd.read_csv('C:/Users/User/Downloads/LINE WORKS/Summarize_Public_data_final.csv',encoding='utf-8-sig')
newdata = pd.DataFrame()
notempty = df[df.keyword!=np.nan]
df.keyword = df.keyword.fillna('')
for i in list_:
    need = df.loc[df.keyword.str.contains(i)]
    newdata = pd.concat([newdata, need])
newdata.drop_duplicates('title', inplace=True)



newdata.to_csv('after.csv', index=False,encoding='utf-8-sig')