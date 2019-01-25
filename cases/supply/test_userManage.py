import sys,os,json,pytest
from interfaceFrameWork.requestsTemp import requestsTemp
from interfaceFrameWork.entity.tools import jsonLoad
from interfaceFrameWork.entity.connectDB import dbConn

def test_addNormalUser():
    supplyDB = dbConn("supply")
    supplyName = jsonLoad().getVariable("supply/userManage.json","deleteUser","supplyName")
    userName = jsonLoad().getVariable("supply/userManage.json","deleteUser","userName")
    sql = 'delete from acct_supplier_user where sname="'+supplyName+'" and name ="'+userName+'" and admin = 2'
    res = supplyDB.executeSqlWithSql(sql)
    res = requestsTemp().supplyRequests("supply/userManage.json","addNormalUser")
    assert res["status"] == 1
