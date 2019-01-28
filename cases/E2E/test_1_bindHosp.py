import sys,os,json,pytest,allure
from interfaceFrameWork.requestsTemp import requestsTemp
from interfaceFrameWork.entity.tools import jsonLoad

def test_hospAddBindCode():
    res = requestsTemp().hospRequests("E2E/1_bindHosp.json","hospAddBindCode")
    print(res)
    assert res["code"] == 200
