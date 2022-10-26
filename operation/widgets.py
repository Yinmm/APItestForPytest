from core.result_base import ResultBase
from api.pet_V2 import widgets
from common.logger import logger


def widgets_update(token, language="cn"):
    """
    小组件获取宠物信息
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    json_data = {
        "lang": language
    }
    res = widgets.widget_update(json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("小组件获取宠物信息 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


# print(login("1testt", "123456", "11"))

