import sys,os,json,pytest
from interfaceFrameWork.requestsTemp import requestsTemp
from interfaceFrameWork.entity.tools import jsonLoad,getTime

initResult = jsonLoad().jsonContext("init.json")
hid = initResult["hospital"]["hid"]
sid = initResult["supply"]["sid"]

extraParams = {}

def test_hospAddOrder():
    extraParams={}
    nowTime = getTime().getYYYYMMDDTimestamp()
    extraParams["orderDate"] = nowTime
    res = requestsTemp().hospRequests("E2E/4_orderFlow.json","hospAddOrder",extraParams=extraParams)
    assert res["code"] == 200

def test_hospSendOrder():
    needSendOrderList = requestsTemp().hospRequests("E2E/4_orderFlow.json","hospGetSendingOrder")
    orderId = needSendOrderList["page"]["list"][0]["id"]
    orderNo = needSendOrderList["page"]["list"][0]["orderNo"]
    extraParams["id"] = orderId
    res = requestsTemp().hospRequests("E2E/4_orderFlow.json","hospSendOrder",extraParams=extraParams)
    assert res["code"] == 200

# def test_supplyConfrimOrder():
#     extraParams["hid"] = hid
#     needConfirmOrderList = requestsTemp().supplyRequests("E2E/4_orderFlow.json","supplyGetNeedConfirmOrder",extraParams=extraParams)
#     orderId = needConfirmOrderList["result"]["data"][0]["id"]
#     orderNo = needConfirmOrderList["result"]["data"][0]["num"]
#     extraParams["orderNo"] = orderNo
#     extraParams["oid"] = orderId
#     needConfirmOrderList = requestsTemp().supplyRequests("E2E/4_orderFlow.json","supplyConfirmOrder",extraParams=extraParams)
#     assert needConfirmOrderList["status"] == 1




# test_supplyConfrimOrder()