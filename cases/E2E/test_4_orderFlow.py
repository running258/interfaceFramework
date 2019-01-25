import sys,os,json,pytest
from interfaceFrameWork.requestsTemp import requestsTemp
from interfaceFrameWork.entity.tools import jsonLoad,getTime

def test_hospAddOrder():
    extraParams={}
    nowTime = getTime().getTimestamp()
    extraParams["orderDate"] = nowTime
    res = requestsTemp().hospRequests("E2E/4_orderFlow.json","hospAddOrder")
    assert res["code"] == 200

def test_hospSendOrder():
    needSendOrderList = requestsTemp().hospRequests("E2E/4_orderFlow.json","hospGetSendingOrder")
    orderId = needSendOrderList["page"]["list"][0]["id"]
    orderNo = needSendOrderList["page"]["list"][0]["orderNo"]
    extraParams={}
    extraParams["id"] = orderId
    res = requestsTemp().hospRequests("E2E/4_orderFlow.json","hospSendOrder",extraParams=extraParams)
    assert res["code"] == 200

def test_supplyConfrimOrder():
    needSendOrderList = requestsTemp().hospRequests("E2E/4_orderFlow.json","hospGetSendingOrder")
    orderId = needSendOrderList["page"]["list"][0]["id"]
    orderNo = needSendOrderList["page"]["list"][0]["orderNo"]
    extraParams={}
    extraParams["id"] = orderId
    res = requestsTemp().hospRequests("E2E/4_orderFlow.json","hospSendOrder",extraParams=extraParams)
    assert res["code"] == 200

test_supplyConfrimOrder()