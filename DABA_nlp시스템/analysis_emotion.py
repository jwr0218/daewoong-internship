# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:01:11 2020

@author: User
"""




from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics
# import text_wordcloud
from sklearn.naive_bayes import MultinomialNB 
from sklearn.pipeline import Pipeline 
from sklearn.feature_extraction.text import TfidfVectorizer, HashingVectorizer, CountVectorizer

from wordcloud import WordCloud 
import matplotlib.pyplot as plt

from PIL import Image
from collections import Counter
import numpy as np 
import pandas as pd 



def emotion(lst):
    # 좋아요  / 훈훈해요 / 슬퍼요 / 화나요 / 후속기사 원해요
    result = 0 ; 
    emotion=(lst[0]+lst[1])-(lst[3]+lst[2])
    if emotion > 0:
        result = 1
    elif emotion <0:
        result = 0 
    else :
        result = -1
        #meaningless
    return result 

import konlpy.tag 

import nltk


okt = konlpy.tag.Okt()

def tokenize(docs):     
    a = []
    
    count = 0
    for t in okt.pos(docs,norm = True ,  stem = True   ):
        
        a.append("/".join(t))
        
    
    return a 




class emotion_analysis():
    
    def __init__(self):
        
        self.df = "Please input your train data" 
        
        
        # test / train split 해야 함 ~!!
#       self.tokenized = 
        
        self.X = []
        self.Y = []
        
        
        self.model = "Not Yet Model is defined"
        
        
        self.frequency = []
        
        self.trainX = []
        self.trainY = []
        
        self.NLTK = []        
        
    def traindata(self,df):
        self.df = df
        
        for i,row in df.iterrows():
            try:
                
                self.X.append(tokenize(row[0]))
                self.Y.append(row[-1])
            except TypeError:
                pass
                                      
        
        
        print(len(self.Y))

        print(len(self.X))            
        
        tokens =  [t for d in self.X for t in d]
        
        
        self.NLTK = nltk.Text(tokens, name='NMSC')
        self.frequency = [f[0] for f in self.NLTK.vocab().most_common(1000)]
        
        self.trainX = [self.term_frequency(i) for i in self.X]        
        
        
        self.trainX = np.asarray(self.trainX).astype('float32')
        
        
        print(self.trainX.shape)
        
        
        
        self.trainY = np.asarray(self.Y).astype('float32')
        
        
    
    
    def term_frequency(self,lst):
        find = []
        for f in self.frequency:
            try:
                find.append(Counter(lst)[f])
            except KeyError:
                find.append(0)
        return find
    
    
    
    
    
    
    
    

    
    def naiveBayes(self):
        
        bayes = MultinomialNB()
    
        bayes.fit(self.trainX,self.trainY)
        
            
        print(bayes.predict(self.trainX))
    
        return bayes
    
    
    def define_Model(self):
        
        
        
        
        
        self.model = models.Sequential()    
        self.model.add(layers.Dense(64, activation='relu', input_shape=(1000,)))
        self.model.add(layers.Dense(64, activation='relu'))
        self.model.add(layers.Dense(1, activation='sigmoid'))
        
        self.model.compile(optimizer=optimizers.RMSprop(lr=0.001),
            loss=losses.binary_crossentropy,
            metrics=[metrics.binary_accuracy])
        
        self.model.fit(self.trainX, self.trainY, epochs=10, batch_size=512)
        
        results = self.model.evaluate(self.trainX, self.trainY)
        
        print(results)
        
        return self.model

    def predict_pos_neg(self,review):
        token = tokenize(review)
        tf = self.term_frequency(token)
        data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
        score = float(self.model.predict(data))
        
        if score > 0.5:

            return "[{}]는 {:.2f}% 확률로 긍정적 key 문장으로 예측 됩니다.\n".format(review, score * 100)
        return "[{}]는 {:.2f}% 확률로 부정적 key 문장으로 예측 됩니다.\n".format(review, (1 - score) * 100)










'''     
emT = emotion_analysis()
    
emT.traindata(testData)    

model = emT.define_Model()

emT.predict_pos_neg("아리까리 하네요. 저는 이 영화 추천 드리지는 않습니다.")

emT.predict_pos_neg("올해 최고의 영화! 세 번 넘게 봐도 질리지가 않네요.")

emT.predict_pos_neg("하,,, 뭐냐,,, 이영화 ㄹㅇ 개빡치게 하네 개졸았다 ㄹㅇ로")

emT.predict_pos_neg("주연 배우가 신인인데 연기를 진짜 잘 하네요. 몰입감 ㅎㄷㄷ")

bayes = emT.naiveBayes()
'''