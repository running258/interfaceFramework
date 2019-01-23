import requests, json,os,sys

curPath = os.path.abspath(os.path.realpath(__file__))
prePath = os.path.split(curPath)[0]
sys.path.append(prePath)

from login import Login
from entity.tools import jsonLoad,getTime

class requestsTemp(Login):

    def supplyRequests(self, jsonFile, dataNode,*, returnType = "json", extraParams={}):
        authorization = Login().supplyLogin()
        jsonContext = jsonLoad().jsonContext(jsonFile)
        data = jsonContext[dataNode]
        method = data["method"]
        path = data["path"]
        header = data["header"]
        header["authorization"] = authorization
        params = data["params"]
        params["_t"] = getTime().getTimestamp()
        params = {**params, **extraParams}  # merge the params and update params by extraParams 

        if method.lower() == "post":
            params = json.dumps(params)
            res = requests.post(self._supplyUrl+path, data=params,headers=header)
        elif method.lower() == "get":
            print(self._supplyUrl+path)
            print(header)
            print(params)
            res = requests.get(self._supplyUrl+path, params=params,headers=header)
            print(res.url)
        elif method.lower() == "put":
            res = requests.put(self._supplyUrl+path, data=params,headers=header)
        else:
            raise Exception("no requests named %s"% (method))

        # return different type of response with returnType
        if returnType.lower() == "json":
            return res.json()
        elif returnType.lower() == "string" or returnType.lower() == "text":
            return res.text

    def person(self):
        pass

