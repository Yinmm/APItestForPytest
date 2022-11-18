from core.result_base import ResultBase
from api.pet_V2 import role
from common.logger import logger


def get_init_type(token):
    """
    获取初始宠物类型
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = role.init_type(headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("获取初始宠物类型 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def create(token, name, master_name):
    """
    创建角色
    :param name: 宠物名
    :param master_name: 主人名
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "name": name,
        "master_name": master_name,
        "pet_type_id": 1
    }
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = role.create(json=json_data, headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("创建角色 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def info(token):
    """
    获取初始宠物详情
    :param token: token值
    """
    result = ResultBase()
    header = {
         "Content-Type": "application/json",
         "token": token
    }
    res = role.info(headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("获取宠物详情 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def update(token):
    """
    刷新宠物信息
    :param token: token值
    """
    result = ResultBase()
    header = {
         "Content-Type": "application/json",
         "token": token
    }
    res = role.update(headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("刷新宠物信息 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def change_pet_name(token, name):
    """
    修改宠物名
    :param token
    :param name: 宠物名
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "name": name
    }
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = role.change_pet_nickname(json=json_data, headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("修改宠物名 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def change_master_name(token, master_name):
    """
    修改宠物名
    :param token
    :param master_name: 主人名
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "name": master_name
    }
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = role.change_owner_nickname(json=json_data, headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("修改宠物名 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result






# print(login("1testt", "123456", "11"))

