# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:40:27 2020

@author: User
"""



from newspaper import Article
from konlpy.tag import Kkma
from konlpy.tag import Twitter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import normalize
import numpy as np

class SentenceTokenizer(object):
    def __init__(self):
        self.kkma = Kkma()
        self.twitter = Twitter()
        self.stopwords = ['중인' ,'만큼', '마찬가지', '꼬집었', "연합뉴스", "데일리", "동아일보", "중앙일보", "조선일보", "기자","아", "휴", "아이구", "아이쿠", "아이고", "어", "나", "우리", "저희", "따라", "의해", "을", "를", "에", "의", "가",]
    def url2sentences(self, url):
        article = Article(url, language='ko')
        article.download()
        article.parse()
        sentences = self.kkma.sentences(article.text)
        for idx in range(0, len(sentences)):
            if len(sentences[idx]) <= 10:
                sentences[idx-1] += (' ' + sentences[idx])
                sentences[idx] = ''
        return sentences
    def text2sentences(self, text):
        sentences = self.kkma.sentences(text)
        for idx in range(0, len(sentences)):
            if len(sentences[idx]) <= 10:
                sentences[idx-1] += (' ' + sentences[idx])
                sentences[idx] = ''
        return sentences
    def get_nouns(self, sentences):
        nouns = []
        for sentence in sentences:
            if sentence is not '':
                nouns.append(' '.join([noun for noun in self.twitter.nouns(str(sentence))
                                           if noun not in self.stopwords and len(noun) > 1]))
        return nouns

class GraphMatrix(object):
    def __init__(self):
        self.tfidf = TfidfVectorizer()
        self.cnt_vec = CountVectorizer()
        self.graph_sentence = []
    def build_sent_graph(self, sentence):
        tfidf_mat = self.tfidf.fit_transform(sentence).toarray()
        self.graph_sentence = np.dot(tfidf_mat, tfidf_mat.T)
        return self.graph_sentence
    def build_words_graph(self, sentence):
        cnt_vec_mat = normalize(self.cnt_vec.fit_transform(sentence).toarray().astype(float), axis=0)
        vocab = self.cnt_vec.vocabulary_
        return np.dot(cnt_vec_mat.T, cnt_vec_mat), {vocab[word] : word for word in vocab}





class Rank(object):
    def get_ranks(self, graph, d=0.85): # d = damping factor
        A = graph
        matrix_size = A.shape[0]
        for id in range(matrix_size):
            A[id, id] = 0 # diagonal 부분을 0으로
            link_sum = np.sum(A[:,id]) # A[:, id] = A[:][id]
            if link_sum != 0:
                A[:, id] /= link_sum
            A[:, id] *= -d
            A[id, id] = 1
        B = (1-d) * np.ones((matrix_size, 1))
        ranks = np.linalg.solve(A, B) # 연립방정식 Ax = b
        return {idx: r[0] for idx, r in enumerate(ranks)}


class TextRank(object):
    def __init__(self, a):
        self.sent_tokenize = SentenceTokenizer()
        self.sentences = a.values.tolist()
        self.nouns = self.sent_tokenize.get_nouns(self.sentences)
        self.graph_matrix = GraphMatrix()
        self.sent_graph = self.graph_matrix.build_sent_graph(self.nouns)
        self.words_graph, self.idx2word = self.graph_matrix.build_words_graph(self.nouns)
        self.rank = Rank()
        self.sent_rank_idx = self.rank.get_ranks(self.sent_graph)
        self.sorted_sent_rank_idx = sorted(self.sent_rank_idx, key=lambda k: self.sent_rank_idx[k], reverse=True)
        self.word_rank_idx = self.rank.get_ranks(self.words_graph)
        self.sorted_word_rank_idx = sorted(self.word_rank_idx, key=lambda k: self.word_rank_idx[k], reverse=True)
    def summarize(self, sent_num=3):
        summary = []
        index=[]
        for idx in self.sorted_sent_rank_idx[:sent_num]:
            index.append(idx)
            index.sort()
        for idx in index:
            summary.append(self.sentences[idx])
        return summary
    def keywords(self, word_num=10):

        rank = Rank()
        rank_idx = rank.get_ranks(self.words_graph)
        sorted_rank_idx = sorted(rank_idx, key=lambda k: rank_idx[k], reverse=True)
        print(type(rank_idx))
        keywords = []
        index=[]
        for idx in sorted_rank_idx[:word_num]:
            index.append(idx)
            #index.sort()

            #dic key 값 ( 인덱스  ) 다 뽑았음 이제 key 값 바탕으로 corelation 찾아서 넣기 
            
        for idx in index:
            keywords.append(self.idx2word[idx])
        
        return keywords
    
    


# 일반 코드보단 이걸 사용하는게 더 문맥에 맞는 알고리즘을 사용하는 결과를 창출할 것이다. 
# 기사 본문을 keyword 로 뽑아서 바꾸는 것 . 
        
    

#textrank = TextRank('데이터프레임을 to String 으로 하나의 문단 화 할 것  또한 이 메소드를 여기다 쓸 것이 아니라 실제로 사용 할 곳에 import 시킬 것')







# url 대신 text를 입력 가능 하다. 



'''
for row in textrank.summarize(10):
    print(row)
    print()
    print("==========================")
print('keywords :',textrank.keywords())
    
'''

''' 워드 크라우드 예시 코드 '''

from wordcloud import WordCloud 
import matplotlib.pyplot as plt
from konlpy.tag import Hannanum
from PIL import Image



def wordcloud_textmining(text):
        

    H = Hannanum()
    twttierMS = np.array(Image.open('./static/images/동그라미.png'))
    
    
    a = " ".join(H.nouns(text))
    wc = WordCloud(font_path = "./font/BMEULJIROTTF.ttf"
                ,background_color = "white"
                ,width = 1000, height = 1000  
                ,mask = twttierMS
                ,max_words = 150
                ,max_font_size = 200 )

    wc.generate(a)


    fig = plt.figure()
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    
    plt.savefig('./static/Wordcloud.png')
    return fig

#wordcloud_textmining(textrank.summarize(10))
    


        
    

''' 문서 요약 받아서 이 받은 key word 를 바탕으로 frequency algorithm 사용을 한다면? 
좀 더 효과가 좋은 알고리즘이 나올 것 frequency가 맞는 알고리즘인가,,,? '''