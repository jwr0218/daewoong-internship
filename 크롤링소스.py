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


def croller():
    
    dic = {"tag" : [] ,"time" : [], "title" : [] , "columns" : []}
    df1 = pd.DataFrame(dic)
    
    chrome_options = webdriver.ChromeOptions()
   # chrome_options.add_argument('--headless') # gui 없이 돌아갈 수 있게 도와줌 
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')


    driver = webdriver.Chrome('C:/Users/User/Desktop/chromedriver.exe', chrome_options = chrome_options)

    driver.get("https://www.data.go.kr/tcs/dss/selectDataSetList.do") 
    driver.find_element_by_xpath('//*[@id="dTypeFILE"]/a').click()
    time.sleep(1)
            
    
    
    count = 1
    page = 2
    while True:
        
        try:
        # 게시판 !!!
            
            time.sleep(1)
            
            
            # 제목 , tag 뽑기 
            tag = driver.find_element_by_xpath('//*[@id="fileDataList"]/div[2]/ul/li['+str(count)+']/p/span[1]')
                
                    
                                                      
            tag_text = tag.text
            print(tag_text)
                
            title = driver.find_element_by_xpath('//*[@id="fileDataList"]/div[2]/ul/li['+str(count)+']/dl/dt/a/span[2]')
            title_text = title.text 
            print(title_text)
            
            driver.find_element_by_xpath('//*[@id="fileDataList"]/div[2]/ul/li['+str(count)+']/dl/dt/a').send_keys(Keys.CONTROL +"\n")  
            
            
            
            T1 = driver.find_element_by_xpath('//*[@id="fileDataList"]/div[2]/ul/li['+str(count)+']/div[1]/p[1]/span[2]').text
            #                                   //*[@id="fileDataList"]/div[2]/ul/li[2]/div[1]/p[1]/span[2]
            print(T1)
            '''새창 띄우기''' 
            
            
            
            #title.send_keys(Keys.CONTROL +"\n")  
            
            
            
            driver.switch_to.window(driver.window_handles[1])
            
            
            time.sleep(1)
           
            # column 뽑기
            lst = ""
            span_turn = 1
            
            while True:
                
                
                try:
                    
                    span = driver.find_element_by_xpath('//*[@id="contents"]/div[2]/div[2]/div[2]/div/table/tbody/tr[1]/td['+ str(span_turn) +']/span')
                    lst = lst+"  \ "+span.text
                   
                    span_turn = span_turn+1
                    
                    
                except NoSuchElementException:
                    
                    break
             
            #데이터프레임에 넣어야 함
            print(lst)
            dic = {"tag" : [tag_text] ,"time" : [T1], "title" : [title_text] , "columns" : [lst]}
            df = pd.DataFrame(dic)
            df1 = pd.concat([df1,df])
            
            #새창 닫기
            
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            
            
        #게시판 ---
        #목록 하나 내려가기
             
            count = count +1
            
        #다 뽑앗으면?
            if count > 10:
            
                
                try:
                    print("----------------")
                    time.sleep(1)
                    
                    
                    driver.find_element_by_xpath('//*[@id="fileDataList"]/nav/a['+str(page)+']').click()
                    
                    if page >= 11:
                        
                        
                        count = 1 
                        page = 2
                        
                        
                    else:
                        count = 1 
                        page = page +1      
                        print(page)
                        
                
                except NoSuchElementException:
                    

                    break    
                #여기서 보내기 
                
                
                
                
                
           
        except NoSuchElementException:
            print(df1)
            
            
            break
        
    return df1



if __name__ == "__main__":
    print(croller())
    
    