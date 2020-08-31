from flask import Flask, request, Response , render_template , url_for
import  text_wordcloud
import pandas as pd 
import pymysql
import urllib.request 
from analysis_emotion import emotion_analysis
import base64 
from base64 import b64encode 
import io 
import requests
from matplotlib.backends.backend_agg import FigureCanvasAgg

app = Flask(__name__)
import DBase as DB

db = DB.DBmysql()

keywords = []
a = db.extractData('')
EM = emotion_analysis()

a['title'] = a['title'].astype(str)+ "."

a = a.drop_duplicates(['title'])
textrank = text_wordcloud.TextRank(a['title'])    
keywords = textrank.keywords()  

traindata = a[['title','emotion']]
EM.traindata(traindata)

model = EM.define_Model()

summarize = ""

textdata = []
@app.route('/')
def Keyword_wordcloud():
    


    #summarize = textrank.summarize(10)
   
    return render_template('main.html', textrank = keywords )



@app.route("/Details", methods = ['POST'])
def detail():
    
    value = request.form['Keyword']
    
    if value == "":
        return "뽑고자 하는 keyword와 연관된 데이터가 존재하지 않습니다."
    
    try:

        data = db.extractData(value)
    except:
        return "Data which related to keyword is empty"
    
    
    data = data.drop_duplicates(['title'])
    data['title'] = data['title'].astype(str)+ "."
    
    detail_textrank = text_wordcloud.TextRank(data['title'])    

    summarize = detail_textrank.summarize(10)
    
    data =" ".join(summarize)


    find = summarize[:4]

    lst = []
    for i in summarize:

        lst.append(EM.predict_pos_neg(i))
    
    
    
    

   
   
    
    

    return render_template('detail.html', summarize=find,data = data , emotion = lst , textrank = keywords )

@app.route('/plot/<vendor_duns>')
def plot(vendor_duns):
    fig = text_wordcloud.wordcloud_textmining(vendor_duns)
    
        
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    
    return Response(output.getvalue(), mimetype='image/png')

#if __name__ == '__main__':
app.run()