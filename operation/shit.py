from core.result_base import ResultBase
from api.pet_V2 import shit
from common.logger import logger


def shit_info(token):
    """
    获取屎信息
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = shit.shit_info(headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("获取屎信息 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def shit_clean(token, list):
    """
    清理屎
    :param token: token值
    :param list: 屎id列表
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    json_data =list
    res = shit.shit_clean(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("清理屎 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

# print(login("1testt", "123456", "11"))

