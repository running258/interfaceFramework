import pymysql
from tools import jsonLoad

class dbConn(object):

    def __init__(self, env="staging", jsonFile="init.json"):

        self.connEnv = jsonLoad().jsonContext(jsonFile)["dbConn"][env]

    def connectToSupply(self):

        host = self.connEnv["host"]
        port = self.connEnv["port"]
        username = self.connEnv["username"]
        password = self.connEnv["password"]
        dbName = self.connEnv["supplyDB"]

        pass

dbConn()