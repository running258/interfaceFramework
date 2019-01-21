import requests, json
from login import Login
from entity.tools import jsonLoad,getTime

class requestsTemp(Login):

    def supplyRequests(self, jsonFile, dataNode, returnType = "json", ):
        authorization = Login().supplyLogin()
        jsonContext = jsonLoad().jsonContext(jsonFile)
        data = jsonContext[dataNode]
        method = data["method"]
        path = data["path"]
        header = data["header"]
        header["authorization"] = authorization
        params = data["params"]
        params["_t"] = getTime().getTimestamp()

        if method.lower() == "post":
            params = json.dumps(params)
            res = requests.post(self._supplyUrl+path, data=params,headers=header)
        elif method.lower() == "get":
            res = requests.get(self._supplyUrl+path, data=params,headers=header)
        elif method.lower() == "put":
            res = requests.put(self._supplyUrl+path, data=params,headers=header)
        else:
            raise Exception("no requests named %s"% (method))

        if returnType.lower() == "json":
            return res.json()
        elif returnType.lower() == "string" or returnType.lower() == "text":
            return res.text
