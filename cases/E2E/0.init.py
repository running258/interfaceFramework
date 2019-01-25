import sys,os,json,pytest
from interfaceFrameWork.requestsTemp import requestsTemp
from interfaceFrameWork.entity.tools import jsonLoad
from interfaceFrameWork.entity.connectDB import dbConn

hospOrgId = "10053"

def test_initTest():
    hospDB = dbConn("hosp")
    deleteVenCode = "delete from dict_vendor where ven_code='interfaceTest' and org_id="+hospOrgId
    hospDB.executeSqlWithSql(deleteVenCode)



test_initTest()
