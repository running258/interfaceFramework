from interfaceFrameWork.dao.getMongo import mongoConn

class getLoginEnvMongoDB(mongoConn):

    def __init__(self):
        self.db = mongoConn().getConnection()

    def getLoginEnvCollection(self,sys,env="staging"):
        result = self.db.loginEnv.find_one({"sys":sys,"env":env})
        return result
