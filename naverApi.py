import urllib.request
import json
import pandas as pd
def searchbook(title):
    #애플리케이션 클라이언트 id 및 secret
    client_id =  'pf3_DU5ojLmnp_xMFyKi'
    client_secret =  'iJnJmagr1a'
    dis = 100 #몇개 보여드릴까요?
    start = 500 #어디서 부터 시작하나요?
    
    #도서검색 url
    url = "https://openapi.naver.com/v1/search/book.json"
    option = "&display="+str(dis)+"$start={"+str(start)+"}&sort=count"    
    query = "?query="+urllib.parse.quote(title)
    url_query = url + query + option
        
    #Open API 검색 요청 개체 설정
    request = urllib.request.Request(url_query)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    
    #검색 요청 및 처리
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode == 200):
        return response.read().decode('utf-8')
    else:
        return None
 
#검색 결과 항목 정보 출력하기
def item_to_dataframe(item):
    
    dic = {"제목" : [item['title']], "설명" : [item['description']] , "url" : [item['link']],"date" : [item['pubdate']]}
    return  pd.DataFrame(dic)
    
#프로그램 진입점
def main():
    #검색 키워드 요청
    res = searchbook(input("질의:"))
    if(res == None):
        print("검색 실패!!!")
        exit()
    #검색 결과를 json개체로 로딩
    jres = json.loads(res)
    if(jres == None):
        print("json.loads 실패!!!")
        exit()
 
    #검색 결과의 items 목록의 각 항목(post)을 출력
    df = pd.DataFrame({"제목" : [], "설명" : [] , "url" : [],"date" : [] } ) 
    
    for post in jres['items']:
        df = pd.concat([df,item_to_dataframe(post)])
    
    print(df)
    return df
    
#진입점 함수를 main으로 지정
if __name__ == '__main__':
    df = main()
    
    text = df[['제목']]
    
    
    
    
    
    