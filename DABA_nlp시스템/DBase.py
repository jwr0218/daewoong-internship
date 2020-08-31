import pymysql
import pandas as pd 
from datetime import datetime, date
from sqlalchemy import create_engine


    
    


def Emotion(lst):
    lst = lst.lstrip('[')
    lst = lst.rstrip(']')
    lst = lst.replace('\'',"")
    
    lst = lst.split(',')
  
    lst =  list(map(int, lst))


    
  
    var = int(lst[0])+int(lst[1])-int(lst[2])-int(lst[3])
    
    if var > 0:
        return 1
    
    else:
        return 0 


class DBmysql():
    def __init__(self):
        user = 'root'
        password = '1234'
        database = 'daewoong'
        self.engine = create_engine(f'mysql+pymysql://{user}:{password}@127.0.0.1:3306/{database}?charset=utf8mb4')

        self.db= self.engine.connect()
        self.cursor = pymysql.connect(host='localhost',
                                  user='root',
                                  password='1234',
                                  db='daewoong',
                                  ).cursor()
    
    
        
    def extractData(self, condition):

        query = "SELECT * FROM daewoong_marketing where title like '%"+condition+"%' "        
        #order by time
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        result = pd.DataFrame(myresult, columns=[ 'title', 'time', 'body','lst'])
        result = result.drop_duplicates()
        
        result['emotion'] = result.apply(lambda  x : Emotion(x['lst']),axis = 1)
        
        result.drop(['lst'],axis = 1 )

        return result
    
    def drop_duplicates_Mysql (self):
        query = " delete from daewoong_marketing where link not in ( select link from (select link from daewoong_marketing group by title ) as link )"

        self.cursor.execute(query)


    def upload ( self, data ):
        #데이터프레임 넣기 
        data.to_sql(name= "daewoong_marketing" , con=self.engine, if_exists='append',index = False)

        
    
    def commit(self):
        self.db.commit()
    
    
    def close(self):
        self.db.close()

    def Is_this_new(self,condition):
        result = False
        fi = self.extractData(condition)
        
         # 여기서 아무것도 없어서 작동이 되지 않았음.
        
        try:
            da = fi[['date']][-1:].values[0,0] # -1이 아님,... sort시켜야 할 듯 . 
            da  = datetime.strptime(da,'%Y.%m.%d')
            if (datetime.now()-da).days < 3:
                result = True
                return result
            
        except IndexError:
            return result 


