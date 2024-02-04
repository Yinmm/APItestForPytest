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
        # 关闭数据库连接，
        # TODO 在del调用数据库close方法不会生效，会导致程序一直不退出，具体原因暂不清楚，后续解决
        self.conn.close()

    def select_home(self, aid):
        #查询
        a = self.db.get_collection("home").find_one({"_id": ObjectId(aid)})
        self.conn.close()
        return a
    def select_items(self,aid):
        a = self.db.get_collection("items").find_one({"_id": ObjectId(aid)})
        self.conn.close()
        return a

    def update(self, coll="account", acid=''):
        self.db.get_collection(coll).update_one({"_id": ObjectId(acid)}, {"$set": {'gm': True}}) #添加GM
        self.conn.close()  # 在del里调用该函数不生效，所以先放在这里，保证程序在运行完退出


mongodb = MongoDB()

# mongodb.update(acid="63fd75949947c986f5d86897")
# mongodb.select("63ea3909f1f984c3902ec34b")
# test.update("account", "63db0e5852addd586045fcee")