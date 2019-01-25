import os
import json
import time,datetime

class jsonLoad(object):

    def __init__(self):
        self.jsonPath = os.path.abspath('.')+"/docs/data/"

    def jsonContext(self, jsonFileName):
        with open(self.jsonPath+jsonFileName,'r') as jsonContext:
            return json.load(jsonContext)

    def getVariable(self, jsonFileName, dataNode, varName):
        with open(self.jsonPath+jsonFileName,'r') as jsonContext:
            return json.load(jsonContext)[dataNode]["variable"][varName]

class getTime(object):

    def getTimestamp(self):
        return int(time.time())*1000

    def getYYYYMMDDTimestamp(self):
        nowTime = datetime.datetime.now()
        time_structure = datetime.datetime(nowTime.year, nowTime.month, nowTime.day, 8, 0, 0, 0)
        return int(time.mktime(time_structure.timetuple()))*1000


getTime().getYYYYMMDDTimestamp()
