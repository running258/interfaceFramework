import pymysql,os,sys

curPath = os.path.abspath(os.path.realpath(__file__))
prePath = os.path.split(curPath)[0]
sys.path.append(prePath)

from tools import jsonLoad

class dbConn(object):

    def __init__(self,client, env="staging", jsonFile="init.json"):

        self.connEnv = jsonLoad().jsonContext(jsonFile)["dbConn"][env]
        self.client = client

    def connectToSupply(self):

        host = self.connEnv["host"]
        port = self.connEnv["port"]
        username = self.connEnv["username"]
        password = self.connEnv["password"]
        dbName = self.connEnv["supplyDB"]

        db = pymysql.connect(host=host,user=username,password=password,database=dbName,port=port)
        return db

    def connectToHosp(self):
    
        host = self.connEnv["host"]
        port = self.connEnv["port"]
        username = self.connEnv["username"]
        password = self.connEnv["password"]
        dbName = self.connEnv["hospDB"]

        db = pymysql.connect(host=host,user=username,password=password,database=dbName,port=port)
        return db

    def executeSqlWithSql(self,sql):
        if self.client == "supply":
            db = self.connectToSupply()
        elif self.client == "hosptial" or self.client == "hosp" or self.client == "hos":
            db = self.connectToHosp()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            db.commit()
        except:
            db.rollback()
        finally:
            db.close()

        return results
