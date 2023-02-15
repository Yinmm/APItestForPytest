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
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
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
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
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
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("获取工作奖励 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def work_recall(token):
    """
    工作中召回
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = work.work_recall(headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("工作中召回 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def lobby(token):
    """
    小游戏大厅
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    res = work.lobby(headers=header)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("游戏大厅 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def game_start(token, game_id, is_multiple):
    """
    游戏开始
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    data = {
        "game_id": game_id,
        "is_multiple": is_multiple
    }
    res = work.game_start(headers=header, json=data)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("游戏开始 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def game_over(token, game_uid, score):
    """
    游戏结算
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    data = {
        "game_uid": game_uid,
        "score": score
    }
    res = work.game_over(headers=header, json=data)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("游戏结算 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def game_over_ad(token, game_uid):
    """
    游戏结算-广告
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    data = {
        "game_uid": game_uid
    }
    res = work.game_over_ad(headers=header, json=data)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("游戏结算-广告 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def achievement_rewards(token, game_uid):
    # TODO 该接口还未完成
    """
    游戏结算-广告
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    data = {
        "game_uid": game_uid
    }
    res = work.achievement_rewards(headers=header, json=data)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("游戏成就 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def rank(token, game_id):
    """
    排行
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    data = {
        "game_id": game_id
    }
    res = work.rank(headers=header, json=data)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("游戏排行 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def rank_like(token, game_id, target_aid):
    """
    排行
    :param token: token值
    """
    result = ResultBase()
    header = {
        "Content-Type": "application/json",
        "token": token
    }
    data = {
        "game_id": game_id,
        "target_aid": target_aid
    }
    res = work.rank_like(headers=header, json=data)
    if res.status_code != 200:
        logger.info("接口出错，状态码 ==>> {}".format(res.status_code))
    result.success = False
    if res.json()["code"] == "SUCCESS":
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["data"])
    result.msg = res.json()["data"]
    result.response = res
    logger.info("排行榜点赞 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result

# print(login("1testt", "123456", "11"))

print(job_lobby(
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzY4ODEwNzUsImp0aSI6IjYzZTlmMjMzNTFmZGQ4NDk3NmFkMTYyNSIsImFpZCI6IjYzZTlmMWRhNDZhNDVhNmNmMzNkNmYwYSJ9.0JJYQVoH7ZzYhuSTFXPMTmZpnFMiM0ZQV5vqJiVcB6I"))
