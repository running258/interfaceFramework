import os,sys,configparser
curPath = os.path.abspath(os.path.realpath(__file__))
prePath = os.path.split(curPath)[0]
sys.path.append(prePath)
from pymongo import MongoClient

class getConfIni(object):

    def __init__(self):
        curPath = os.path.dirname(os.path.realpath(__file__))
        confPath = os.path.join(curPath, "..\..\conf.ini")
        self.config = configparser.ConfigParser()
        self.config.read(confPath,encoding="utf-8")

class mongoConn(getConfIni):

    def getConnection(self):
        host = self.config.get("mongodb","host")
        port = self.config.get("mongodb","port")
        dbName = self.config.get("mongodb","dbName")
        client = MongoClient(host=host, port=int(port))
        db = client[dbName]
        return db

