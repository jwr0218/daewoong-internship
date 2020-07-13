# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 09:21:30 2020

@author: User
"""
import txtmining as TM 
import naverApi as NP
import konlpy.tag
import pprint

if __name__ == "__main__" :
    
    komoran = konlpy.tag.Komoran()
    
    
    df = NP.main()
    
    data = df[['제목']].to_string(index = False)
    
    #여기서 data는 데이터프레임
    
    #스트링화 시켜야함
    
    txt = komoran.nouns(data)
    
    
    txt = " ".join(txt)
    
    
    find = TM.listupKeyword(TM.preprocessing(txt))
    
    pprint.pprint(find)