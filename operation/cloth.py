from core.result_base import ResultBase
from api.pet_V2 import cloth
from common.logger import logger


def cloth_save(token, data):
    """
    保存穿戴
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    data_json = data
    res = cloth.cloth_save(json=data_json, headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("保存穿戴信息 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result



