import time
import pytest
import os
import allure
from requests.structures import CaseInsensitiveDict
import requests

# from api.pet_V2 import account
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

#
# # 请求前设置加密签名
# def pytest_runtest_protocol(item, nextitem):
#     # 获取测试函数
#     test_function = item.function
#
#     # 检查测试函数是否有 'request' 参数
#     if 'request' in test_function.__code__.co_varnames:
#         # 获取请求体
#         payload = getattr(test_function, 'request', None)
#
#         if payload:
#             # 加密请求体得到sign
#             encrypted_body = encrypt_body(payload)
#             headers = {'Check-Sign': encrypted_body}
#             headers = {'Check-Time': encrypted_body}
#             headers = {'Check-Nonce': encrypted_body}
#             headers = {'Protocol-Version': encrypted_body}
#             headers = {'token': encrypted_body}
#             # 设置请求头
#             setattr(test_function, 'headers', headers)


"""
def test_example(request):
    # 获取加密后的请求头
    headers = getattr(request.function, 'headers', {})

    # 发送请求
    url = 'https://your.api.endpoint'
    response = requests.post(url, json=request, headers=headers)

    # 在这里可以添加断言，检查响应是否符合预期
    assert response.status_code == 200
    assert 'expected_content' in response.text

"""


@allure.step("前置步骤 ==>> 清理数据")
def step_first():
    logger.info("******************************")
    logger.info("前置步骤开始 ==>> 清理数据")


@allure.step("后置步骤 ==>> 清理数据")
def step_last():
    logger.info("后置步骤开始 ==>> 清理数据")


@allure.step("前置步骤 ==>> 管理员用户登录")
def step_login(username, password):
    logger.info("前置步骤 ==>> 管理员 {} 登录，返回信息 为：{}".format(username, password))


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
    step_login(username, password)
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


@pytest.fixture(scope="function")
def delete_register_user():
    """注册用户前，先删除数据，用例执行之后，再次删除以清理数据"""
    del_sql = base_data["init_sql"]["delete_register_user"]
    db.execute_db(del_sql)
    step_first()
    logger.info("注册用户操作：清理用户--准备注册新用户")
    logger.info("执行前置SQL：{}".format(del_sql))
    yield
    db.execute_db(del_sql)
    step_last()
    logger.info("注册用户操作：删除注册的用户")
    logger.info("执行后置SQL：{}".format(del_sql))


def login_2_delete():
    username = "apitest"
    password = "123456"
    # 注册账号
    account.register(username, password)
    # 登录
    login_result = login(username, password)
    # 实名
    # 创角
    # 注销
    pass




@pytest.fixture(scope="session", autouse=True)
def login():
    username = "lc-1"
    password = "123456"
    login_result = account.login(username, password)
    # 将获取到的信息保存到session中
    # request.config.cache.set("login_info", login_result)
    return login_result


@pytest.fixture
def request_hook(request, login):
    token = login.response.json()["data"]["token"]
    aid = login.response.json()["data"]["account_id"]
    random = login.response.json()["data"]["random"]
    version = 19  # 临时

    def hook_before_request(request):
        # 获取请求的 body
        request_body = request.config.cache.get("request_body", None)
        if request_body is None:
            request_body = ""
        # 进行加密操作并返回加密sign、t、uuid
        handle_sign, uuid, t = HandleSign(random, token, aid, version, request_body).to_sign()

        # 从 request.config 获取保存的信息，或者在之前的 fixture 中设置
        headers = CaseInsensitiveDict(request.config.cache.get("request_headers", {}))
        # headers = {}
        headers["Check-Sign"] = handle_sign
        headers["Check-Time"] = t
        headers["Check-Nonce"] = uuid
        headers["Protocol-Version"] = str(version)
        headers["token"] = token
        headers = dict(headers)
        return headers

        # 将 headers 保存到 request.config 以供后续测试使用
        # request.config.cache.set("request_headers", headers)
    return hook_before_request(request)


@pytest.fixture
def make_request(request_hook):
    # 这个 fixture 负责实际发送请求
    def send_request(request_function, *args, **kwargs):
        response = request_function(*args, headers=request_hook, **kwargs)
        return response
    return send_request


