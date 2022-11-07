import time

import pytest
import allure
from operation.role import update
from operation.gm import *
from common.redis_operate import redis_db
from common.logger import logger
from testcases.conftest import pet_data, account_id
from data.pet.global_config import get_pet_config


@allure.step("前置步骤 ==>> 设置数据")
def step_data_value(init_hunger, interval_time, reduce_value, except_value):
    logger.info(
        "前置步骤===>初始值-{},间隔时间(时间衰减单位)-{},每衰减时间单位减少值-{},预期结果-{}"
        .format(init_hunger, interval_time, reduce_value, except_value))


@allure.step("前置步骤 ==>> 设置数据")
def step_health_data_value(hunger, mood, clean, init_value, interval_time, reduce_value, except_value):
    logger.info(
        "前置步骤===>饥饿值初始值-{},心情值初始值-{},清洁值初始值-{},健康值初始值-{}间隔时间(时间衰减单位)-{},每衰减时间单位减少值-{},预期结果-{}"
        .format(hunger, mood, clean, init_value, interval_time, reduce_value, except_value))


@allure.step("前置步骤 ==>> 设置数据")
def step_weight_data_value(hunger, mood, health, interval_time, except_value):
    logger.info(
        "前置步骤===>饥饿值-{},心情值-{},健康值-{},间隔时间(时间衰减单位)-{},预期结果-{}"
        .format(hunger, mood, health, interval_time, except_value))


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("数值模块")
class TestData(object):
    """数值模块"""

    @allure.story("用例--饥饿值数值测试")
    @allure.description("该用例是饥饿值数值的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("init_value, interval_time", pet_data["test_data"])
    def test_hunger_data(self, pet_login_hasrole_fixture, init_value, interval_time):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        update(token)
        gm = GM(token)
        gm.gm_hunger(init_value)
        gm.moditem_list()
        now_timestamp = redis_db.get_hunger_timestamp(account_id)
        reduce = int(get_pet_config.get_HungerConfig()["reduce"])
        except_data = init_value - int(interval_time * reduce)
        if except_data < 0:
            except_data = 0
        set_timestamp = now_timestamp - interval_time * get_pet_config.get_HungerConfig()["time"]
        redis_db.set_hunger_timestamp(account_id, int(set_timestamp))
        redis_db.set_system_timestamp(account_id, int(set_timestamp))  # 系统时间也要一起修改
        step_data_value(init_value, interval_time, reduce, except_data)
        result = update(token)
        assert result.response.status_code == 200
        if result.response.json().get("code") == "SUCCESS":
            items = result.response.json().get("data").get("items")
            for i in items:
                if i.get("item_id") == 102:
                    logger.info(
                        "hunger ==>> 期望结果：{}， 实际结果：{}".format(except_data, i.get("number")))
                    assert i.get("number") == except_data
        else:
            logger.info("*************** 返回结果错误 ***************")
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--清洁值数值测试")
    @allure.description("该用例是清洁值数值的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("init_value, interval_time", pet_data["test_data"])
    def test_clean_data(self, pet_login_hasrole_fixture, init_value, interval_time):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        update(token)
        gm = GM(token)
        gm.gm_clean(init_value)
        gm.moditem_list()
        now_timestamp = redis_db.get_clean_timestamp(account_id)
        reduce = int(get_pet_config.get_CleanConfig()["reduce"])
        except_data = init_value - int(interval_time * reduce)
        if except_data < 0:
            except_data = 0
        set_timestamp = now_timestamp - interval_time * get_pet_config.get_CleanConfig()["time"]
        redis_db.set_clean_timestamp(account_id, int(set_timestamp))
        redis_db.set_system_timestamp(account_id, int(set_timestamp))  # 系统时间也要一起修改
        step_data_value(init_value, interval_time, reduce, except_data)
        result = update(token)
        assert result.response.status_code == 200
        if result.response.json().get("code") == "SUCCESS":
            items = result.response.json().get("data").get("items")
            for i in items:
                if i.get("item_id") == 101:
                    logger.info(
                        "hunger ==>> 期望结果：{}， 实际结果：{}".format(except_data, i.get("number")))
                    assert i.get("number") == except_data
        else:
            logger.info("*************** 返回结果错误 ***************")
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--心情值数值测试")
    @allure.description("该用例是心情值数值的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("init_value, interval_time", pet_data["test_data"])
    def test_mood_data(self, pet_login_hasrole_fixture, init_value, interval_time):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        update(token)
        gm = GM(token)
        gm.gm_mood(init_value)
        gm.moditem_list()
        now_timestamp = redis_db.get_mood_timestamp(account_id)
        reduce = int(get_pet_config.get_MoodConfig()["reduce"])
        except_data = init_value - int(interval_time * reduce)
        if except_data < 0:
            except_data = 0
        set_timestamp = now_timestamp - interval_time * get_pet_config.get_MoodConfig()["time"]
        redis_db.set_mood_timestamp(account_id, int(set_timestamp))
        redis_db.set_system_timestamp(account_id, int(set_timestamp))  # 系统时间也要一起修改
        step_data_value(init_value, interval_time, reduce, except_data)
        result = update(token)
        assert result.response.status_code == 200
        if result.response.json().get("code") == "SUCCESS":
            items = result.response.json().get("data").get("items")
            for i in items:
                if i.get("item_id") == 100:
                    logger.info(
                        "hunger ==>> 期望结果：{}， 实际结果：{}".format(except_data, i.get("number")))
                    assert i.get("number") == except_data
        else:
            logger.info("*************** 返回结果错误 ***************")
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--健康值数值测试")
    @allure.description("该用例是健康值数值的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("hunger,mood,clean,init_value,interval_time", pet_data["test_health_data"])
    def test_health_data(self, pet_login_hasrole_fixture, hunger, mood, clean, init_value, interval_time):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        update(token)
        gm = GM(token)
        gm.gm_hunger(hunger)
        gm.gm_mood(mood)
        gm.gm_clean(clean)
        gm.gm_heath(init_value)
        gm.moditem_list()
        now_timestamp = redis_db.get_health_timestamp(account_id)
        reduce = 0
        if hunger == 0 and mood == 0 and clean == 0:
            reduce = int(get_pet_config.get_HealthConfig()["reduce_2"])
        elif (hunger == 0 and mood == 0) or (hunger == 0 and clean == 0) or (mood == 0 and clean == 0):
            reduce = int(get_pet_config.get_HealthConfig()["reduce_1"])
        elif hunger == 0 or mood == 0 or clean == 0:
            reduce = int(get_pet_config.get_HealthConfig()["reduce_0"])
        elif hunger != 0 and mood != 0 and clean != 0:
            reduce = 0
        else:
            logger.info("取值错误，请检查用例")
        except_data = init_value - int(interval_time * reduce)
        if except_data < 0:
            except_data = 0
        set_timestamp = now_timestamp - interval_time * get_pet_config.get_HealthConfig()["time"]
        redis_db.set_health_timestamp(account_id, int(set_timestamp))
        redis_db.set_system_timestamp(account_id, int(set_timestamp))  # 系统时间也要一起修改
        step_health_data_value(hunger, mood, clean, init_value, interval_time, reduce, except_data)
        result = update(token)
        assert result.response.status_code == 200
        if result.response.json().get("code") == "SUCCESS":
            items = result.response.json().get("data").get("items")
            for i in items:
                if i.get("item_id") == 113:
                    logger.info(
                        "hunger ==>> 期望结果：{}， 实际结果：{}".format(except_data, i.get("number")))
                    assert i.get("number") == except_data
        else:
            logger.info("*************** 返回结果错误 ***************")
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--体重数值测试")
    @allure.description("该用例是体重数值的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("hunger,mood,health,interval_time", pet_data["test_weight_data"])
    def test_weight_data(self, pet_login_hasrole_fixture, hunger, mood, health, interval_time):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        re = update(token)
        items = re.response.json().get("data").get("items")
        current_weight = 0
        max_weight = 0
        for i in items:
            if i.get("item_id") == 116:
                max_weight = i.get("number")
                current_weight = max_weight
        gm = GM(token)
        gm.gm_weight(max_weight)
        gm.gm_hunger(hunger)
        gm.gm_mood(mood)
        gm.gm_heath(health)
        gm.moditem_list()
        now_timestamp = redis_db.get_weight_timestamp(account_id)
        weight_up = get_pet_config.get_WeightUp()["value"]
        weight_up_time = get_pet_config.get_WeightUp()["time"]
        weight_down = get_pet_config.get_WeightDown()["value"]
        weight_down_time = get_pet_config.get_WeightDown()["time"]
        except_data = 0
        set_timestamp = 0
        if health == 0:
            except_data = current_weight
            set_timestamp = now_timestamp - interval_time * weight_up_time
        elif hunger == 0:
            except_data = current_weight - weight_down * interval_time
            logger.info("每单位时间减少：{}点".format(weight_down))
            if except_data < max_weight * (100-get_pet_config.get_WeightDownLimit()["max_reduce"])/100:
                except_data = max_weight * (100-get_pet_config.get_WeightDownLimit()["max_reduce"])/100
            set_timestamp = now_timestamp - interval_time * weight_down_time
        elif hunger > 0:
            weight_up_config = get_pet_config.get_WeightUpMood()
            for i in weight_up_config:
                rate = i["rate"]
                range_min = i["range"][0]
                range_max = i["range"][1]
                if range_min <= mood <= range_max:
                    except_data = current_weight + int(weight_up * ((100 + rate) / 100) * interval_time)
                    logger.info("每单位时间加成百分点为{}".format(rate))
                    logger.info("每单位时间增加：{}点".format(weight_up * ((100 + rate) / 100)))
                    break
            set_timestamp = now_timestamp - interval_time * weight_up_time
        if except_data < 100:
            except_data = 100
        redis_db.set_weight_timestamp(account_id, int(set_timestamp))
        redis_db.set_system_timestamp(account_id, int(set_timestamp))  # 系统时间也要一起修改
        step_weight_data_value(hunger, mood, health, interval_time, except_data)
        except_data = int(except_data)
        result = update(token)
        assert result.response.status_code == 200
        if result.response.json().get("code") == "SUCCESS":
            items = result.response.json().get("data").get("items")
            for i in items:
                if i.get("item_id") == 115:
                    logger.info(
                        "hunger ==>> 期望结果：{}， 实际结果：{}".format(except_data, i.get("number")))
                    assert i.get("number") == except_data
        else:
            logger.info("*************** 返回结果错误 ***************")
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    """
    -k:可指定参数，参数为字符串格式，该字符串参数的目的是用来部分或全部匹配测试用例名称。使用该选项，pytest仅会收集测试用例名称中包含参数的测试用例执行测试
    -m:用于执行符合指定标记的测试用例
    -s:显示print内容
    -x:遇到第一个失败用例即可终止测试
    –maxfail=num:可以指定遇到第几个失败用例时，才会停止测试
    -if:运行上一个测试中失败的用例
    -ff:与–lf相比，会执行所有用例，但是会把之前失败的用例由优先执行
    -v:可以使得测试输出更加详细。直观的一点，加上该选项，测试输出中会把用例名打印出来
    -q:与-v的作用相反，会简化输出信息
    -i:用例执行失败时，打印出其局部变量
    """
    pytest.main()
    # os.system(r"allure generate -c -o allure-report")
    # pytest.main(["test_01_register.py", "--clean-alluredir"])

    # allure generate ./json -o ./report --clean //生成测试报告
    #
    # allure open report --host 192.168.1.165 --port 8800 //打开报告 host = 本机ip
