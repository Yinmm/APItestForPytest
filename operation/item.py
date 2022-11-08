from core.result_base import ResultBase
from api.pet_V2 import item
from common.logger import logger


def item_buy(token, Class, itme_id, number):
    """
    购买物品
    :param token: token值
    :param Class: 大类id
    :param itme_id: 物品id
    :param number: 购买数量
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    json_data = {
        "class": Class,
        "item_id": itme_id,
        "number": number
    }
    res = item.buy(json=json_data, headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("购买物品 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def item_list(token):
    """
    物品列表
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = item.item_list(headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("物品列表 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def item_use(token, Class, itme_id):
    """
    使用物品
    :param token: token值
    :class:物品大类ID
    :item_id:物品id
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    json_data = {
        "class": Class,
        "item_id": itme_id
    }
    res = item.item_use(json=json_data, headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("使用物品 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

# print(login("1testt", "123456", "11"))

