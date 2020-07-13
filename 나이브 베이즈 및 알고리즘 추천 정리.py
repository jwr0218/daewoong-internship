# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 10:25:24 2020

@author: User
"""


from sklearn.feature_extraction.text import CountVectorizer
import pprint

vectorizer = CountVectorizer()


lst = ['첫번째 테스트','두번째 테스트','세번째 테스트','네번째 테스트','다섯번째 테스트','여섯번째 테스트']

vectorizer.fit(lst)
pprint.pprint(vectorizer.vocabulary_ )


testTXT = ["첫번째 테스트 임함.","두번째 테스트 임함","세번째 테스트 임함","네번째 테스트 임함","다섯째 테스트 임함"]

cs = vectorizer.transform(testTXT)


#------------------------------특정 단어가 얼마나 반복되는가? 정도를 계산하는 것. -----------------------

# komoran() 메소드와 같이 쓰이면 상당히 효과적일 것으로 예상



from sklearn.naive_bayes import MultinomialNB



classifier = MultinomialNB()


label = [0,0,0,1,1]
classifier.fit(cs.toarray(),label)

# 실험 결과,각 단어에 포함되지 않는 단어들이 있는데, 이들도 올바른 학습값, 0 으로 진행하는 경우가 있다. 
#이를 해결하기 위해 garbage in, out 이 실행되야 하는 것으로 예상된다.
# how ??.... searching 

# 받은 문장을 SPLIT 시킴 IN 함수를 써 TRUE값을 가지는 데이터들만을 분류, 합침. 그리고 transform 을 하면 값의 정확도가 높아질 수 있음.


    




txtNew = "여섯째 망했엉 ㅠ"

newTxt = vectorizer.transform([txtNew])

pprint.pprint(newTxt.toarray())

print(classifier.predict(newTxt.toarray()))

print(classifier.predict_proba(newTxt))



# 나이브 베이즈 클래시파이어로, 감정분석 LABEL 을 만들고 난 후 , 감정분석을 진행 


# 가장 많이 출현되는 빈도수와 감정분석 결과 긍정적 요소를 가지는 것들을 분류 

# 알고리즘을 만들어 처리하는 방법 




