import pymysql
from tools import jsonLoad

class dbConn(object):

    def __init__(self, env="staging", jsonFile="init.json"):

        self.connEnv = jsonLoad().jsonContext(jsonFile)["dbConn"][env]

    def connectToSupply(self, jsonFileName):
        pass

dbConn()