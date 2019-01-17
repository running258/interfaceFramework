import requests
import json
from tools import jsonLoad
from tools import getTime

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

        self.supplyLoginRoute = "/api1/auth/login"
        self.hospLoginRoute = "/sys/login"

        # self.loginParams = {}
        self.roleFile = "supply/roleManage.json"

    def supplyLogin(self, jsonFile="init.json"):
        loginInfo = jsonLoad().jsonContext(jsonFile)
        userName = loginInfo["supply"]["userName"]
        passWord = loginInfo["supply"]["passWord"]
        loginParams = {"identifier":userName,"password":passWord,"_t":getTime().getTimestamp()}
        res = requests.post(self._supplyUrl+self.supplyLoginRoute,data=loginParams)
        authorization = json.loads(res.text)["result"]["token"]
        header = {"authorization":authorization}
        
        roleListContext = jsonLoad().jsonContext(self.roleFile)
        roleListRoute = roleListContext["roleList"]["url"]
        params = {"_t":getTime().getTimestamp()}
        res = requests.get(self._supplyUrl+roleListRoute,headers=header,data=params)
        return header
