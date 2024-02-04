from core.result_base import ResultBase
from api.pet_V2 import account
from common.logger import logger


def register(username, password):
    """
    注册用户信息
    :param username: 用户名
    :param password: 密码
    :param hardware: 设备
    """
    result = ResultBase()
    json_data = {
        "username": username,
        "password": password,
        "hardware": "pc",
    }
    header = {
        "Content-Type": "application/json"
    }
    res = account.register(json=json_data, headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("注册用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def login(username, password):
    """
    登录用户
    :param username: 用户名
    :param password: 密码
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "username": username,
        "password": password,
        "channel": 0
    }
    header = {
        "Content-Type": "application/json"
    }
    res = account.login(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
        result.token = res.json()["data"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def get_new_token(token):
    """
    获取新token
    :param token
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = account.get_new_token(headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("获取新token ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def id_card_auth(token, op_id, id_no, name):
    """
    实名认证
    :param token
    :param op_id: 操作码cd
    :param id_no: 身份证号码
    :param name: 姓名
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    json_data = {
        "op_id": op_id,
        "id_no": id_no,
        "name": name
    }
    res = account.id_card_auth(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("实名认证 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

# register("tt123", "12345", "1")
