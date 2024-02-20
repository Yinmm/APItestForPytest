import time
import pytest
import os
import allure
import json

from api.user import user
from operation import account, role
from common.mongodb_operate import mongodb
from common.read_data import data
from common.logger import logger
from common.handle_sign import HandleSign
from data.pet.pet_config import get_pet_config

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    try:
        data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
        yaml_data = data.load_yaml(data_file_path)
    except Exception as ex:
        pytest.skip(str(ex))
    else:
        return yaml_data


base_data = get_data("base_data.yml")
pet_data = get_data("pet/pet_test_data.yml")
pet_config = get_pet_config

# account_id = base_data["test_account_hasrole"]["account_id"]



@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@pytest.fixture(scope="session")
def login_fixture():
    username = base_data["init_admin_user"]["username"]
    password = base_data["init_admin_user"]["password"]
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {
        "username": username,
        "password": password
    }
    loginInfo = user.login(data=payload, headers=header)
    yield loginInfo.json()


@allure.step("前置步骤 ===> 用户注册+登录")
def step_pet_register(username):
    logger.info("前置步骤===>用户：{}注册+登录".format(username))


@allure.step("前置步骤 ===> 用户登录")
def step_pet_login(username):
    logger.info("前置步骤===>用户：{}注册-登录-实名-创建角色".format(username))


@pytest.fixture(scope="session")
def pet_login_hasrole_fixture():
    username = base_data["test_account_hasrole"]["username"]
    password = base_data["test_account_hasrole"]["password"]
    # 注册
    account.register(username, password, "1")
    # 登录
    res = account.login(username, password, 1)
    loginInfo = res.response.json()
    id_no = "445221200208221626"
    personname = "test"
    token = loginInfo["data"]["token"]
    acid = loginInfo["data"]["account_id"]
    # 实名
    account.id_card_auth(token, str(time.time()), id_no, personname)
    # 创角
    role.create(token, "pet", "master")
    # 添加GM权限
    mongodb.update(acid=acid)
    # 再次登录
    res = account.login(username, password, 1)
    loginInfo = res.response.json()
    step_pet_login(username)
    yield loginInfo


@pytest.fixture(scope="session")
def pet_login_norole_fixture(username, password, hardware, channel):
    register_data = {
        "username": username,
        "password": password,
        "hardware": hardware
    }
    login_data = {
        "username": username,
        "password": password,
        "hardware": channel
    }
    header = {
        "Content-Type": "application/json"
    }
    account.register(json=register_data, headers=header)
    loginInfo = account.login(json=login_data, headers=header)
    step_pet_register(username)
    yield loginInfo.json()


@pytest.fixture(scope="session", autouse=True)
def login():
    username = "lc-1"
    password = "123456"
    login_result = account.login(username, password)
    # 将获取到的信息保存到session中
    # request.config.cache.set("login_info", login_result)
    return login_result


@pytest.fixture
def request_hook(login):
    token = login.response.json()["data"]["token"]
    aid = login.response.json()["data"]["account_id"]
    random = login.response.json()["data"]["random"]
    version = 19  # 临时

    def hook_before_request(request_body):
        if request_body is None:
            request_body = ""
        # 进行加密操作并返回加密sign、t、uuid
        handle_sign, uuid, t = HandleSign(random, token, aid, version, request_body).to_sign()
        headers = {}
        headers["Check-Sign"] = handle_sign
        headers["Check-Time"] = t
        headers["Check-Nonce"] = uuid
        headers["Protocol-Version"] = str(version)
        headers["token"] = token
        headers = dict(headers)
        return headers

        # 将 headers 保存到 request.config 以供后续测试使用
        # request.config.cache.set("request_headers", headers)
    return hook_before_request


@pytest.fixture
def make_request_header(request_hook):
    # 这个 fixture 负责实际发送请求
    def send_request(request_function, *args, **kwargs):
        request_body = dict(**kwargs).get("json")
        # 将字典对象转换为 JSON 格式的字符串,不转字符串的话，加密body出错
        json_str = json.dumps(request_body)
        response = request_function(headers=request_hook(json_str), data=json_str)
        return response
    return send_request


