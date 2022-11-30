from core.result_base import ResultBase
from api.pet_V2 import LuckyTree
from common.logger import logger
import json

def luckytree_info(token):
    """
    获取摇钱树信息
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = LuckyTree.luck_tree_info(headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("获取摇钱树信息 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def luckytree_reward(token,is_ad):
    """
    获取摇钱树信息
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    json_data = {
        "is_ad": is_ad
    }
    res = LuckyTree.luck_tree_rewards(json=json_data, headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("获取摇钱树奖励 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

