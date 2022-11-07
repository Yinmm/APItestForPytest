import time

import pytest
import allure
from operation.role import update
from operation.gm import *
from common.redis_operate import redis_db
from common.logger import logger
from testcases.conftest import pet_data, account_id
from data.pet.global_config import get_pet_config

@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("数值模块")
class TestData(object):
    """数值模块"""

    @allure.story("用例--饥饿值数值测试")
    @allure.description("该用例是饥饿值数值测试的测试")
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
        except_data = init_value - int(interval_time*int(get_pet_config.get_HungerConfig()["reduce"]))
        if except_data < 0:
            except_data = 0
        set_timestamp = now_timestamp - interval_time*get_pet_config.get_HungerConfig()["time"]
        redis_db.set_hunger_timestamp(account_id, int(set_timestamp))
        redis_db.set_system_timestamp(account_id, int(set_timestamp)) #系统时间也要一起修改
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

