# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 16:35:55 2020

@author: User
"""

import pandas as pd 


from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException, TimeoutException,StaleElementReferenceException
import urllib.request
import requests
from datetime import datetime 
import time as time
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.action_chains import ActionChains
def crawller():
    
    
    chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument('--headless') # gui 없이 돌아갈 수 있게 도와줌 
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome('C:/Users/User/Desktop/chromedriver.exe', chrome_options = chrome_options)
#//*[@id="conditionBtn"]
    driver.get("https://emed.mfds.go.kr/#!CECAC01F010") 
    
        
    
    driver.implicitly_wait(10)
            
    
    '''
    제조의뢰자상호 제조의뢰국 제조의뢰자소재지 제조자상호 제조국 제조자소재지 등급 품목군 발급기관 유효기간
    '''
    dic = {"순번" : [] , "업소명" : [] ,"업종구분" : [] ,"업허가번호": [],"유효기간":[] 
           ,"제조의뢰자 상호" : [],"제조의뢰국" : [],"제조의뢰자소재지" : [],"제조자상호" : []
           ,"제조국" : [],"제조자소재지" : [],"등급" : [],"품목군" : [],"발급기관" : []}
    
    df1 = pd.DataFrame(dic)
    
    
    count = 1
    page = 1
    while True:
        
        try:
            
            driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div/div/div/div[5]/input').send_keys("\b\b\b\b"+str(page)+" \n")
            time.sleep(1)
        # 게시판 !!!
                
           # wait.until(ExpectedConditions.stalenessOf(By. ));
            number = driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr['+str(count)+']/td[1]').text
                
            
            
                                                   
            name = driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr['+str(count)+']/td[2]').text
            tp = driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr['+str(count)+']/td[3]').text            
            assigned_number = driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr['+str(count)+']/td[4]').text
            valid_date = driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr['+str(count)+']/td[5]').text
            
            
            print(number , name , tp , assigned_number , valid_date)
            
            
            go = driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr['+str(count)+']') 
            
            actions = ActionChains(driver)                                           
            
            actions.double_click(go)
            actions.perform()
            
            
            driver.implicitly_wait(5)
            
            tags = [
                driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[1]').text
                    ,driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[2]').text
                    ,driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[3]').text
                    ,driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[4]').text
                    ,driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[5]').text
                    ,driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[6]').text
                    ,driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[7]').text
                    ,driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[8]').text
                    ,driver.find_element_by_xpath('//*[@id="civil-content"]/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div[3]/table/tbody/tr/td[9]').text
                    ]
            
            dic = {"순번" : [number] , "업소명" : [name] ,"업종구분" : [tp] ,"업허가번호": [assigned_number],"유효기간":[valid_date] 
           ,"제조의뢰자 상호" : [tags[0]],"제조의뢰국" : [tags[1]],"제조의뢰자소재지" : [tags[2]],"제조자상호" : [tags[3]]
           ,"제조국" : [tags[4]],"제조자소재지" : [tags[5]],"등급" : [tags[6]],"품목군" : [tags[7]],"발급기관" : [tags[8]]}
            #                                   //*[@id="fileDataList"]/div[2]/ul/li[2]/div[1]/p[1]/span[2]
            
            
            # column 뽑기
           
            
            
            
            #데이터프레임에 넣어야 함
            print("---------------------",count,"===================")
            df = pd.DataFrame(dic)
            print(df)
            df1 = pd.concat([df1,df])
            
            df1.to_csv("C:/Users/User/Desktop/testtest.csv",encoding='utf-8-sig')
            
            #새창 닫기
            
            driver.back()
         
            count = count +1
            
            
            
            
        #다 뽑앗으면?
            if count > 10:
                count = 1
                page = page+1
                
                
                print('======넘어갑니다.=======')
                
                
                
                
                
                
           
        except NoSuchElementException as e:
            print(df1)
            print(e)
            
            break
        
    return df1



if __name__ == "__main__":
    a = crawller()
    a.to_csv("C:/Users/User/Desktop/testtest1.csv",encoding='utf-8-sig')
    
