import pytest
import os
import allure
from api.pet_V2 import account
from api.user import user
from common.mysql_operate import db
from common.read_data import data
from common.logger import logger


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
pet_data_register = get_data("pet/pet_test_data.yml")



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
    logger.info("前置步骤===>用户：{}登录".format(username))


@pytest.fixture(scope="session")
def pet_login_hasrole_fixture():
    username = base_data["test_account_hasrole"]["username"]
    password = base_data["test_account_hasrole"]["password"]
    json_data = {
        "username": username,
        "password": password,
        "channel": 1
    }
    header = {
         "Content-Type": "application/json"
    }
    loginInfo = account.login(json=json_data,headers=header)
    step_pet_login(username)
    yield loginInfo.json()


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
