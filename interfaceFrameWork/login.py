import requests, json
from entity.tools import jsonLoad,getTime
from interfaceFrameWork.dao.getLoginEnvMongoDB import getLoginEnvMongoDB

class Login(object):

    def __init__(self, env="staging"):

        if env=="staging":
            self._hospUrl = "https://hosp-cloud.staging.viewchain.net"
            self._supplyUrl = "https://vhsupply.staging.viewchain.net"
        elif env=="test":
            self._hospUrl = "https://hosp-cloud.test.viewchain.net"
            self._supplyUrl = "https://vhsupply.test.viewchain.net"
        elif env=="demo":
            self._hospUrl = "https://hosp-cloud.demo.viewchain.net"
            self._supplyUrl = "https://vhsupply.demo.viewchain.net"
        else:
            raise Exception("the env is INCORRECT! please check your env than try again.")

        self.supplyLoginPath = "/api1/auth/login"
        self.getUserRes = "/api1/api/user/base/getUserRes"
        self.hospLoginPath = "/sys/login"

    def supplyLogin(self, jsonFile="init.json"):
        loginInfo = jsonLoad().jsonContext(jsonFile)
        userName = loginInfo["supply"]["userName"]
        passWord = loginInfo["supply"]["passWord"]
        loginParams = {"identifier":userName,"password":passWord,"_t":getTime().getTimestamp()}
        res = requests.post(self._supplyUrl+self.supplyLoginPath,data=loginParams)
        authorization = json.loads(res.text)["result"]["token"]
        header = {"authorization":authorization}
        
        params = {"_t":getTime().getTimestamp()}
        res = requests.get(self._supplyUrl+self.getUserRes,headers=header,data=params)
        return authorization

    def hospLogin(self, jsonFile="init.json"):
        loginInfo = jsonLoad().jsonContext(jsonFile)
        userName = loginInfo["hospital"]["userName"]
        passWord = loginInfo["hospital"]["passWord"]
        loginParams = {"username":userName,"password":passWord,"captcha":"","checked":False}
        res = requests.post(self._hospUrl+self.hospLoginPath,data=loginParams)
        authorization = json.loads(res.text)["Authorization"]
        return authorization

class LoginWithMongo(object):
    
    def __init__(self, sys,env="staging"):
        result = getLoginEnvMongoDB().getLoginEnvCollection(sys,env)
        self.url = result["url"]
        self.path = result["path"]
        self.userName = result["userName"]
        self.passWord = result["passWord"]

    def supplyLogin(self):
        userName = self.userName
        passWord = self.passWord
        loginParams = {"identifier":userName,"password":passWord,"_t":getTime().getTimestamp()}
        res = requests.post(self.url+self.path,data=loginParams)
        authorization = json.loads(res.text)["result"]["token"]
        header = {"authorization":authorization}
        params = {"_t":getTime().getTimestamp()}
        res = requests.get(self.url+"/api1/api/user/base/getUserRes",headers=header,data=params)
        return authorization

print(LoginWithMongo("supply").supplyLogin())