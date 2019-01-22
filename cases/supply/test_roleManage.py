import sys,os,json,pytest
# sys.path.append("interfaceFrameWork/")
sys.path.append("../../interfaceFrameWork")
from interfaceFrameWork.requestsTemp import requestsTemp
from interfaceFrameWork.entity.tools import jsonLoad

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


# def test_addRole():
#     res = requestsTemp().supplyRequests("supply/roleManage.json","addRole")
#     assert res["status"] == 1

# def test_deleteRole():
#     roleListRes = requestsTemp().supplyRequests("supply/roleManage.json","roleList")
#     roleName = jsonLoad().getVariable("supply/roleManage.json","deleteRole","roleName")
#     rid = (i["id"] for i in roleListRes["result"] if i["name"]==roleName).__next__()
#     params={}
#     params["rid"] = rid
#     deleteRoleRes = requestsTemp().supplyRequests("supply/roleManage.json","deleteRole",extraParams=params)
#     print(deleteRoleRes)

print(sys.path)

