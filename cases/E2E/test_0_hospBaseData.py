import sys,os,json,pytest
from interfaceFrameWork.requestsTemp import requestsTemp
from interfaceFrameWork.entity.tools import jsonLoad

def test_hospAddStore():
    res = requestsTemp().hospRequests("E2E/0_hospBaseData.json","hospAddStore")
    assert res["code"] == 200

def test_hospDeleteStore():
    storeListRes = requestsTemp().hospRequests("E2E/0_hospBaseData.json","hospStoreList")
    storeName = jsonLoad().getVariable("E2E/0_hospBaseData.json","hospDeleteStore","storeName")
    storeId = (i["id"] for i in storeListRes["page"]["list"] if i["warehouseName"]==storeName).__next__()
    extraPath = str(storeId)
    deleteStoreRes = requestsTemp().hospRequests("E2E/0_hospBaseData.json","hospDeleteStore",extraPath=extraPath)
    assert deleteStoreRes["code"] == 200
