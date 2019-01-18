import requests
import json
from entity.tools import jsonLoad
from entity.tools import getTime
from login import Login

class requestsTemp(Login):

    def supplyRequests(self, methods, jsonFile, dataNode):
        authorization = Login().supplyLogin()
        jsonContext = jsonLoad().jsonContext(jsonFile)
        data = jsonContext[dataNode]
        path = data["path"]
        header = data["header"]
        header["authorization"] = authorization
        params = data["params"]
        params["_t"] = getTime().getTimestamp()
        if methods.lower() == "post":
            params = json.dumps(params)
            print(self._supplyUrl+path)
            r = requests.post(self._supplyUrl+path, data=params,headers=header)
        elif methods.lower() == "get":
            r = requests.get(self._supplyUrl+path, data=params,headers=header)
        elif methods.lower() == "put":
            r = requests.put(self._supplyUrl+path, data=params,headers=header)
        else:
            raise Exception("no requests named %s"% (methods))

        print(r.text)

requestsTemp().supplyRequests("post","supply/roleManage.json","addRole")
        