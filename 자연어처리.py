# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:39:16 2020

@author: User
"""

import pprint
import konlpy.tag
import pandas as pd 
import txtmining as TM 
from collections import Counter

'''깃 연습용 테스트 - 업데이트 '''



# df.to_string(index=False)를 사용하면 dataframe을 출력 할 수 있습니다.
# index=False 를 사용하면 맨 앞 컬럼에 자동 생성되는 인덱스 번호를 빼고 출력 할 수 있습니다
#datastring = magic.to_string(index=False)


def tagCount(tag):
    
    
    #지워야 하는 목록들, 전 프로젝트가 영어여서 영어로 했음 하지만 한글로 바꾼다면 의미 있을 것임.
  
    delete = '1,2,3,4,5,6,7,8,9,0,b,c,con,you,call,cant,chance,change,come,cop,could,day,dont,dozen,even,everyone,know,right,f,find,first,feel,fuck,g,give,get,go,good,guy,h,happen,hope,ill,im,ive,leave,let,li,like,live,long,look,lot,made,make,man,many,may,month,much,na,name,need,never,new,number,one,part,people,please,really,said,say,see,shit,somebody,someone,start,still,stop,take,tell,time,th,thank,thing,think,today,tr,tweet,two,u,use,w,watch,water,want,way,word,would,woman,write,yall,year,youre'
    delete = delete.split(',')

    list_preprocessed = [a for a in tag if a not in delete]
    
    counter = Counter(list_preprocessed) # 추가된 리스트를 누적하여 센다
    counter.update(list_preprocessed)
    a = counter.most_common(n=20) # 빈도수가 높은 10개의 키워드를 출력한다
    return a






if __name__ == "__main__":
    
    komoran = konlpy.tag.Komoran()
    
    text = "라틴어로 기병을 의미한다. 고대 로마의 원로원 계급 다음가는 신분이다. 원래는 말에 타고 군무에 종사하는 사람을 의미하였기에 이런 이름이 붙었으나, 점차 일정한 재산과 자격을 구비한 사람이 이 계층에 들게 되고 그것이 세습신분화 되어 로마사회의 하급 지배계층으로 굳어지게 된다. 초기 로마 왕국의 군사제도에서는 병사 자신의 재산으로 무장을 구입해야 했기 때문에 말을 사서 무장할 수 있을 정도의 재산가만이 에퀴테스가 될 수 있었다. 후에 군제 개편에 의해 로마가 직업군인제로 바뀌면서 기병이라는 의미보다는 큰 재산을 지닌 사회적 지배계급으로서의 의미가 강해지게 되는데, 사실 그 이전부터 군대의 규모가 커짐에 따라 에퀴테스가 아닌 일반 부유평민들이 기병으로 대거 들어오면서 기병으로서의 정체성이 많이 흐려지게 된 반면, 군대 내 여러 장교직들을 거의 배타적으로 맡게되는등 아래 평민신분들과는 차별화된 우대를 받았으며 이외에도 사회적으로는 상업이나 광업등의 사업을 대규모로 운영하며 큰 부를 축적했기 때문이다. 또한 에퀴테스들은 자신들의 튜닉에 좁은 띠로 자수를 놓아 신분을 표시할 수 있었데, 이것이 로마군내 장교보직의 명칭에 반영되기도 하였다.[1]과거 카이사르가 기병 부족으로 허덕일 때 굴러다니던 게르만족 기병을 로마 기병으로 고용하자, 그 게르만인들은 자신들을 인정해준 카이사르를 위하여 열심히 노력했다. 카이사르의 게르만 기병대는 사실상 카이사르의 충복 중에서도 핵심 충복으로 일컬을 정도였다.로마 공화국 말기에는 점차 로마의 직업군인이 차별대우를 받으면서 동시에 에퀴테스들이 상업이나 무역 등에 종사한다는 것을 빌미로 원로원 계급은 그들의 신분에 걸맞지 않는다 하여 상업이나 무역 등에 종사하는 것에 한동안 금지당했었던 반면(lex claudia), 에퀴테스들은 국가사업이나 징세 등의 역할 또한 맡아 활발히 활동했다.로마 제국 시기에는 황제의 원로원 계급을 견제하려는 목적 때문에 황제 직속의 궁정 관료로서의 위치까지 점하였으나, 제국의 쇠퇴와 더불어 점차 정치적 힘을 잃었다.공화주의자였던 키케로가 이 신분 출신이었다."
    
    
    
    # dataframe 을 연관성 분석을 진행하려면 dataframe이름.to_string(index=False) 를 해야함 
    find = TM.listupKeyword(TM.preprocessing(text))
    
