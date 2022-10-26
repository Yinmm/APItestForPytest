from core.result_base import ResultBase
from api.pet_V2 import work
from common.logger import logger


def work_info(token):
    """
    获取工作信息
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = work.work_info(headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("获取工作信息 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def work_start(token):
    """
    开始工作
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = work.work_start(headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("开始工作 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def work_reward(token):
    """
    获取工作奖励
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = work.work_reward(headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("获取工作奖励 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

# print(login("1testt", "123456", "11"))

