from core.result_base import ResultBase
from api.pet_V2 import gm, item


class GM(object):
    """
    GM命令类
    """
    def __init__(self, token):
        self.token = token

    def get_item_list(self):
        header = {
            "Content-Type": "application/json",
            "token": self.token
        }
        res = item.item_list(headers=header)
        return res.json()["data"]["items"]

    def moditem(self, data_json):
        """
        主修改方法
        :param data_json：传入json数据
        :return: 自定义的关键字返回结果 result
        """
        result = ResultBase()
        header = {
            "Content-Type": "application/json",
            "token": self.token
        }
        res = gm.gm(json=data_json, headers=header)
        result.success = False
        if res.json()["code"] == "SUCCESS":
            result.success = True
        return result

    def gm_gold(self, number):
        data_json = {
            "number": number,
            "item_id": 1,
            "class": 1
        }
        self.moditem(data_json)

    def gm_mood(self, number):
        data_json = {
            "number": number,
            "item_id": 100,
            "class": 1
        }
        self.moditem(data_json)

    def gm_hunger(self, number):
        data_json = {
            "number": number,
            "item_id": 102,
            "class": 1
        }
        self.moditem(data_json)

    def gm_clean(self, number):
        data_json = {
            "number": number,
            "item_id": 101,
            "class": 1
        }
        self.moditem(data_json)

    def gm_heath(self, number):
        data_json = {
            "number": number,
            "item_id": 113,
            "class": 1
        }
        self.moditem(data_json)

    def gm_clean_cloth(self):
        item_list = self.get_item_list()
        for i in item_list:
            if i["class"] == 3:
                data_json = {
                    "number": 0,
                    "item_id": i["item_id"],
                    "class": i["class"]
                }
                self.moditem(data_json)

    def gm_clean_furniture(self):
        item_list = self.get_item_list()
        for i in item_list:
            if i["class"] == 4:
                data_json = {
                    "number": 0,
                    "item_id": i["item_id"],
                    "class": i["class"]
                }
                self.moditem(data_json)
