import os
import json

class jsonLoad(object):

    def __init__(self):
        self.jsonPath = os.path.abspath('.')+"/docs/data/"

    def jsonContext(self, jsonFileName):
        with open(self.jsonPath+jsonFileName,'r') as jsonContext:
            return json.load(jsonContext)
