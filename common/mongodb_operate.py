from bson import ObjectId
import os
from pymongo import MongoClient
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data.load_ini(data_file_path)["mongoDB"]

DB_CONF = {
    "url": data["url"],
    "db": data["db"],
    "user": data["user"],
    "password": data["password"]
}


class MongoDB:

    def __init__(self, URL=DB_CONF["url"], db=DB_CONF["db"], user=DB_CONF["user"], password=DB_CONF["password"]):
        try:
            # 建立连接
            self.url = URL
            self.conn = MongoClient(self.url, password=password, username=user, authSource=db)
            self.db = self.conn[db]
        except Exception as e:
            logger.info("连接mongodb出现错误，错误原因：{}".format(e))

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭数据库连接
        self.conn.close()

    def select(self):
        #查询
        a = self.db.get_collection("account").find({"register.username":"test12"})
        print(a)

    def update(self, coll="account", acid=''):
        self.db.get_collection(coll).update_one({"_id": ObjectId(acid)}, {"$set": {'gm': True}})
        self.conn.close()
        # pass


# key = "luckyTree:637f2c22be4c994db6bc09c5"
# redis_db.del_key(key)
# print(redis_db.redis_conn.exists(key))
# name = "6360bf8ef36c0134564db35c"
# value = "1667783801"
# set = redis_db.set_hunger_timestamp(name, value)
# print(set)

mongodb = MongoDB()

mongodb.update(acid="63db0e5852addd586045fcee")
# test.update("account", "63db0e5852addd586045fcee")
