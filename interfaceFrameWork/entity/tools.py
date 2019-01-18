import os
import json
import time

class jsonLoad(object):

    def __init__(self):
        self.jsonPath = os.path.abspath('.')+"/docs/data/"

    def jsonContext(self, jsonFileName):
        with open(self.jsonPath+jsonFileName,'r') as jsonContext:
            return json.load(jsonContext)

class getTime(object):

    def getTimestamp(self):
        return int(time.time())*1000
