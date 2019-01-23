import sys,os,json,pytest
from interfaceFrameWork.requestsTemp import requestsTemp
from interfaceFrameWork.entity.tools import jsonLoad

def test_addRole():
    res = requestsTemp().supplyRequests("supply/roleManage.json","addRole")
    assert res["status"] == 1

def test_deleteRole():
    roleListRes = requestsTemp().supplyRequests("supply/roleManage.json","roleList")
    roleName = jsonLoad().getVariable("supply/roleManage.json","deleteRole","roleName")
    rid = (i["id"] for i in roleListRes["result"] if i["name"]==roleName).__next__()
    params={}
    params["rid"] = rid
    deleteRoleRes = requestsTemp().supplyRequests("supply/roleManage.json","deleteRole",extraParams=params)
    print(deleteRoleRes)
