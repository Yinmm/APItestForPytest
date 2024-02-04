import gzip
import json

from redis import Redis, ConnectionPool
import os
from common.read_data import data
from common.logger import logger

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
data = data.load_ini(data_file_path)["redis"]

DB_CONF = {
    "host": data["redis_host"],
    "port": int(data["redis_port"]),
    "password": data["redis_password"],
    "db": int(data["redis_DB"])
}


class RedisDB:

    def __init__(self, db_conf=DB_CONF):
        try:
            # 通过字典拆包传递配置信息，建立数据库连接
            redis_pool = ConnectionPool(host=db_conf.get("host"), port=db_conf.get("port"),
                                        password=db_conf.get("password"), db=db_conf.get("db"))
            self.redis_conn = Redis(connection_pool=redis_pool)
        except Exception as e:
            logger.info("连接redis出现错误，错误原因：{}".format(e))

    def __del__(self):  # 对象资源被释放时触发，在对象即将被删除时的最后操作
        # 关闭数据库连接
        self.redis_conn.close()

    def get_value_db(self, key):
        # 获取value
        is_exist = self.redis_conn.exists(key)
        if is_exist == 0:
            return None
        value = self.redis_conn.get(key)
        try:
            value = gzip.decompress(value)
        except:
            value = value.decode('utf-8')
        finally:
            return value

    def get_dict_db(self, key):
        # 获取dict
        is_exist = self.redis_conn.exists(key)
        if is_exist == 0:
            return None
        dict_data = self.redis_conn.hgetall(key)
        new_dict = {}
        for key, value in dict_data.items():
            key = key.decode("utf-8")
            value = value.decode("utf-8")
            new_dict[key] = value
        return new_dict

    # 删除key
    def del_key(self, key):
        self.redis_conn.delete(key)

    # 删除账号的所有key
    def del_all_key(self, aid):
        key_list = ["give_d", "home", "last_request", "shit", "token", "{item}:time", "{item}"]
        for i in key_list:
            key = i + ":" + aid
            self.del_key(key)

    # def set_dict_db(self, key, new_dict):
    #     dict = {}
    #     for key, value in new_dict.items():
    #         key = key.encode("utf-8")
    #         value = value.encode("utf-8")
    #         dict[key] = value
    #     self.redis_conn.hset(key, mapping=dict)

    def set_hash_value(self, name, key, value):
        try:
            key = str(key).encode('utf-8')
            value = str(value).encode('utf-8')
            self.redis_conn.hset(name, key, value)
        except Exception as e:
            logger.info("操作redis出现错误，错误原因：{}".format(e))

    def get_hunger_timestamp(self, key):
        key = "item_time:" + key
        Dict = self.get_dict_db(key)
        return int(Dict["1_102"])

    def get_clean_timestamp(self, key):
        key = "item_time:" + key
        Dict = self.get_dict_db(key)
        return int(Dict["1_101"])

    def get_mood_timestamp(self, key):
        key = "item_time:" + key
        Dict = self.get_dict_db(key)
        return int(Dict["1_100"])

    def get_weight_timestamp(self, key):
        key = "item_time:" + key
        Dict = self.get_dict_db(key)
        return int(Dict["1_115"])

    def get_shit_timestamp(self, key):
        key = "item_time:" + key
        Dict = self.get_dict_db(key)
        return int(Dict["shit"])

    def get_health_timestamp(self, key):
        key = "item_time:" + key
        Dict = self.get_dict_db(key)
        return int(Dict["1_113"])

    def get_system_timestamp(self, key):
        key = "item_time:" + key
        Dict = self.get_dict_db(key)
        return int(Dict["system"])

    def set_hunger_timestamp(self, _key, value):
        key = "item_time:" + _key
        self.set_hash_value(key, "1_102", value)
        return self.get_hunger_timestamp(_key)

    def set_clean_timestamp(self, key, value):
        key = "item_time:" + key
        self.set_hash_value(key, "1_101", value)

    def set_mood_timestamp(self, key, value):
        key = "item_time:" + key
        self.set_hash_value(key, "1_100", value)

    def set_weight_timestamp(self, key, value):
        key = "item_time:" + key
        self.set_hash_value(key, "1_115", value)

    def set_shit_timestamp(self, key, value):
        key = "item_time:" + key
        self.set_hash_value(key, "shit", value)

    def set_health_timestamp(self, key, value):
        key = "item_time:" + key
        self.set_hash_value(key, "1_113", value)

    def set_system_timestamp(self, key, value):
        key = "item_time:" + key
        self.set_hash_value(key, "system", value)


redis_db = RedisDB(DB_CONF)
aid = "644b7efd4c46a8a488e00982"
redis_db.del_all_key(aid)
# print(redis_db.redis_conn.exists(key))
# name = "6360bf8ef36c0134564db35c"
# value = "1667783801"
# set = redis_db.set_hunger_timestamp(name, value)
# print(set)
