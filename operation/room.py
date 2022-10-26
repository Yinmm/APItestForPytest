from core.result_base import ResultBase
from api.pet_V2 import room
from common.logger import logger


def room_get(token):
    """
    获取装修信息
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = room.room_get(headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("获取房间信息 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def room_save(token, list=[]):
    """
    保存装修
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    json_data = {
        "data": list
    }
    res = room.room_save(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("保存装修 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result
