import pytest
from interfaceFrameWork.common.requestsTemp import requestsTemp

def test_addRole():
    res = requestsTemp().supplyRequests("post","supply/roleManage.json","addRole")
    print(res)
    
res = requestsTemp().supplyRequests("post","supply/roleManage.json","addRole")
print(res)
