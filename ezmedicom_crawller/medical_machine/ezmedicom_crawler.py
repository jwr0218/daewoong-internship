# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 08:42:13 2020

@author: User
"""


import pandas as pd 

import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException, TimeoutException,StaleElementReferenceException
import urllib.request
import requests
from datetime import datetime 
import time as time
from selenium.common.exceptions import UnexpectedAlertPresentException

def crawller():
    
    dic = {"업체명" : [] , "품목명" : [] ,"모델명" : [] ,"제품명": [],"품목허가번호":[],"분류번호" : []  ,"등급" : [],"품목허가일자" : [] ,"인체이식형" : [],"일회용" : [],"추적관리대상" : [] ,"한별구성의료기기" : [] ,"조합의료기기" : [] ,"사용 전 멸균필요 " : [] ,"멸균방법" : [] ,"사용목적" : [] ,"저장조건" : [] ,"유통-취급 조건" : [] ,"__기타정보__" : [],"라텍스 포함" : [] ,"프탈에이트류 포함" : [],"자기공명영상(MRI)등에 안전노출" : [],"버전(소프트웨어)" : [],"제품 추가 설명" : [],"요양급여대상" : [],"요양급여코드" : [],"요양 코드 미입력 사유" : [] ,'업허가번호' : [] ,'제조의뢰자' : [],'제조자상호' : []}
    df1 = pd.DataFrame(dic)
    
    chrome_options = webdriver.ChromeOptions()
   # chrome_options.add_argument('--headless') # gui 없이 돌아갈 수 있게 도와줌 
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome('C:/Users/User/Desktop/chromedriver.exe', chrome_options = chrome_options)

    
    driver.maximize_window()


    driver.get("https://udiportal.mfds.go.kr/search/data/P02_01#list") 
    
    driver.implicitly_wait(5)
    
    
    for i in ['수허', '수인', '수신' ,'제허', '제인', '제신'] :
    
        
        driver.find_element_by_name('itemNoFullname').send_keys('\b\b\b\b'+i)
                                       
        driver.find_element_by_xpath('//*[@id="searchBtn"]').click()
        
        
            

        
        count = 0
        page = 3
        
        
        while True:
            
            try:
            # 게시판 !!!
                
                time.sleep(1)
            
                company_name = driver.find_element_by_id('item_'+str(count)).text  
                
                item_name = driver.find_element_by_xpath('//*[@id="itemTr_'+str(count)+'"]/td[2]').text
                
                model_name = driver.find_element_by_xpath('//*[@id="itemTr_'+str(count)+'"]/td[3]').text
                brand_name = driver.find_element_by_xpath('//*[@id="itemTr_'+str(count)+'"]/td[4]').text
                
                assigned_number = driver.find_element_by_xpath('//*[@id="itemTr_'+str(count)+'"]/td[5]').text
                
                driver.find_element_by_id('item_'+str(count)).send_keys("\n") #알기!  
                
                time.sleep(2)
                
                bunryu_number = driver.find_element_by_xpath('//*[@id="mg_meaClassNo"]').text
                
                level = driver.find_element_by_xpath('//*[@id="mg_grade"]').text
                
                date = driver.find_element_by_xpath('//*[@id="mg_permitDate"]').text
                
          
                body_transplant =  driver.find_element_by_xpath('//*[@id="mg_bodyTransplantYn"]').text
                one_use =  driver.find_element_by_xpath('//*[@id="mg_oneuseDevYn"]').text
                trace =  driver.find_element_by_xpath('//*[@id="mg_traceManageTargetYn"]').text
                total_devyn =  driver.find_element_by_xpath('//*[@id="mg_totalDevYn"]').text
                combi_devyn =  driver.find_element_by_xpath('//*[@id="mg_combinationDevYn"]').text
                befor_ster =  driver.find_element_by_xpath('//*[@id="mg_befSterilizationNeedYn"]').text
                method_ster =  driver.find_element_by_xpath('//*[@id="mg_sterilizationMethod"]').text
                use_purpose =  driver.find_element_by_xpath('//*[@id="mg_usePurpose"]').text
                storage_cond =  driver.find_element_by_xpath('//*[@id="mg_storageCond"]').text
                transport_cond =  driver.find_element_by_xpath('//*[@id="mg_distbTreatCond"]').text
                latex_in =  driver.find_element_by_xpath('//*[@id="pg_latexInclsYn"]').text
                phtha_in =  driver.find_element_by_xpath('//*[@id="pg_phthalateInclsYn"]').text
                mri_expsr =  driver.find_element_by_xpath('//*[@id="pg_mriSafeExpsrName"]').text
                pg_swVer_in =  driver.find_element_by_xpath('//*[@id="pg_swVer"]').text
                add_descrip =  driver.find_element_by_xpath('//*[@id="pg_itemAddDescription"]').text
                pg_rcper =  driver.find_element_by_xpath('//*[@id="pg_rcperSalaryTargetYn"]').text
                pg_rcper_code =  driver.find_element_by_xpath('//*[@id="pg_rcperSalaryCode"]').text
                pc_rcper_no_reason =  driver.find_element_by_xpath('//*[@id="pg_rcperSalaryCodeNoinputReas"]').text
                
                
                a =  driver.find_element_by_xpath('//*[@id="pg_meddevEntpNo"]').text
                b =  driver.find_element_by_xpath('//*[@id="pg_manufReqName"]').text
                c =  driver.find_element_by_xpath('//*[@id="pg_manufCltName"]').text
                
                
                dic = {"업체명" : [company_name] , "품목명" : [item_name] ,"모델명" : [model_name] ,"제품명": [brand_name],"품목허가번호":[assigned_number],"분류번호" : [bunryu_number]  ,"등급" : [level],"품목허가일자" : [date] 
                       ,"인체이식형" : [body_transplant],"일회용" : [one_use],"추적관리대상" : [trace] ,
                       "한별구성의료기기" : [total_devyn] ,"조합의료기기" : [combi_devyn] 
                       ,"사용 전 멸균필요 " : [befor_ster] ,"멸균방법" : [method_ster] ,"사용목적" : [use_purpose] ,
                       "저장조건" : [storage_cond] ,"유통-취급 조건" : [transport_cond] ,"__기타정보__" : ["\t | \t"],
                       "라텍스 포함" : [latex_in] ,"프탈에이트류 포함" : [phtha_in],"자기공명영상(MRI)등에 안전노출" : [mri_expsr],
                       "버전(소프트웨어)" : [pg_swVer_in],"제품 추가 설명" : [add_descrip],"요양급여대상" : [pg_rcper],
                       "요양급여코드" : [pg_rcper_code],"요양 코드 미입력 사유" : [pc_rcper_no_reason] 
                       ,'업허가번호' : [a] ,'제조의뢰자' : [b],'제조자상호' : [c]
                       
                       }
                
                df = pd.DataFrame(dic)
                print(df)
                df1 = pd.concat([df1,df])
                
                df1.to_csv("C:/Users/User/Desktop/mfds_data.csv",encoding='utf-8-sig')
                
                
                
                driver.find_element_by_xpath('//*[@id="closeBtnBot"]').click()
                
                
    
                 
                count = count +1
                
                
            #다 뽑앗으면?
                if count > 9:
                    
                    
                    try:
                        print("----------------다음 페이지 ----------------------")
                        driver.implicitly_wait(5)
                        
                        
                        driver.find_element_by_xpath('//*[@id="searchResultList"]/div/div[3]/ul/li['+str(page)+']/a').click()
                       
                            
                        if page >= 7:
                            count = 0 
                            page = 3
                            driver.implicitly_wait(5)
                            
                        else:
                            count = 0 
                            page = page +1      
                            driver.implicitly_wait(5)
                            print("-----------------------------"+str(page-2)+"-----------------------------")
                                    
                    except NoSuchElementException:
                        
    
                        break    
                    #여기서 보내기 
                    
                    
                    
                    
                    
               
            except NoSuchElementException as e:
                print(df1)
                
                print(e)
                
                
                break
        
    return df1




if __name__ == "__main__":
    a = crawller()
    a.to_csv("C:/Users/User/Desktop/mfds_data.csv",encoding='utf-8-sig')
    
