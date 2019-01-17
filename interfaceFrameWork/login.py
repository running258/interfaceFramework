import requests
import json
from interfaceFrameWork.common import jsonLoad

class Login(object):

    def __init__(self, env="staging"):

        if env=="staging":
            self._hospUrl == "https://hosp-cloud.staging.viewchain.net"
            self._supplyUrl == "https://vhsupply.staging.viewchain.net"
        elif env=="test":
            _hospUrl == "https://hosp-cloud.test.viewchain.net"
            self.self._supplyUrl == "https://vhsupply.test.viewchain.net"
        elif env=="demo":
            self._hospUrl == "https://hosp-cloud.demo.viewchain.net"
            self._supplyUrl == "https://vhsupply.demo.viewchain.net"
        else:
            raise Exception("the env is INCORRECT! please check your env than try again.")

        self.supplyLoginRoute = "/api1/auth/login"
        self.hospLoginRoute = "/sys/login"

    def supplyLogin(self, userName, passWord, jsonFile="init.json"):
        context = jsonLoad().jsonContext(jsonFile)
        print(context)


Login().supplyLogin(1,2)
