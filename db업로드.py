import pymysql
import pandas as pd 

from sqlalchemy import create_engine
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
        
    def extractData(self, condition, press):
    
        query = "SELECT * FROM daewoong_crawling_data where company like '%"+condition+"%' and press like '%"+press +"%'"
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        result = pd.DataFrame(myresult)
        
        
        return result
    def extractDataOnlyCompany(self, condition):
    
        query = "SELECT * FROM daewoong_crawling_data where company like '%"+condition+"%' "
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        result = pd.DataFrame(myresult)
        
        
        return result

    def upload ( self, data ):
        data.to_sql(name= "daewoong_crawling_data" , con=self.engine, if_exists='append', index= False)
        
    
    def commit(self):
        self.db.commit()
    
    
    def close(self):
        self.db.close()

item = ['대웅제약', '한미약품', '유한양행', '종근당']

if __name__ == "__main__":


    data = [pd.read_csv('C:\\Users\\User\\Desktop\\site (3)\\news\\data\\대웅제약_total_results.csv'),pd.read_csv('C:\\Users\\User\\Desktop\\site (3)\\news\\data\\유한양행_total_results.csv'),pd.read_csv('C:\\Users\\User\\Desktop\\site (3)\\news\\data\\종근당_total_results.csv'),pd.read_csv('C:\\Users\\User\\Desktop\\site (3)\\news\\data\\한미약품_total_results.csv')]
    db = DBmysql()
    
    for i in [0,1,2,3]:
        data[i]['company'] = item[i]
        db.upload(data[i])
        print(data[i])








   #     self.cursor= self.db.cursor(pymysql.cursors.DictCursor)

'''

    def deleteData (self):
        a = " delete from textdata WHERE d < NOW() - INTERVAL 30 DAY"
        self.cursor.execute(a)
    def extractData(self,condition):
    
        query = "SELECT t FROM textdata where t like '%"+condition+"%'"
        self.cursor.execute(query)
        myresult = self.cursor.fetchall()
        result = pd.DataFrame(myresult)
        
        self.commit()
        return result

'''