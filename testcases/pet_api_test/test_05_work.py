import pytest
import allure
from operation.work import *
from operation.gm import GM
from testcases.conftest import pet_data
from common.logger import logger


@allure.step("前置步骤 ==>> 设置数据")
def step_work(hunger, mood, clean, health):
    logger.info(
        "前置步骤===>前置饥饿值-{},前置心情值-{},前置清洁值-{},前置健康值-{}".format(hunger, mood, clean, health))



@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("工作模块")
class TestWork(object):
    """工作信息模块"""

    @allure.story("用例--获取工作状态")
    @allure.description("该用例是获取宠物工作状态的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    def test_work_info(self, pet_login_hasrole_fixture):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        result = work_info(token)
        # print(result.__dict__)
        assert result.response.status_code == 200
        # assert result.success == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format("SUCCESS", result.response.json().get("code")))
        assert result.response.json().get("code") == "SUCCESS"
        # assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--开始打工")
    @allure.description("该用例是获取宠物开始打工的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("hunger, mood, clean, health, except_code, except_msg",
                             pet_data["test_start_work"])
    def test_start_work(self, pet_login_hasrole_fixture,hunger, mood, clean, health, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        step_work(hunger, mood, clean, health)
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        gm = GM(token)
        gm.gm_mood(mood)
        gm.gm_clean(clean)
        gm.gm_heath(health)
        gm.gm_hunger(hunger)
        gm.moditem_list()
        result = work_start(token)
        assert result.response.status_code == 200
        # assert result.success == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--领取打工奖励")
    @allure.description("该用例是领取打工奖励的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    def test_reward_work(self, pet_login_hasrole_fixture):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        result = work_reward(token)
        # print(result.__dict__)
        assert result.response.status_code == 200
        # assert result.success == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format("NOT_HAVE_WORK_REWARD", result.response.json().get("code")))
        assert result.response.json().get("code") == "NOT_HAVE_WORK_REWARD"
        # assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--打工召回")
    @allure.description("该用例是打工召回的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("except_code", pet_data["test_recall_work"])
    def test_recall_work(self, pet_login_hasrole_fixture, except_code):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        result = work_recall(token)
        assert result.response.status_code == 200
        # assert result.success == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code[0], result.response.json().get("code")))
        assert result.response.json().get("code") == except_code[0]
        # assert except_msg in result.msg
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
    pytest.main(['-q', 'test_05_work.py::TestWork::test_reward_work'])
    # os.system(r"allure generate -c -o allure-report")
    # pytest.main(["test_01_register.py", "--clean-alluredir"])

    # allure generate ./json -o ./report --clean //生成测试报告
    #
    # allure open report --host 192.168.1.165 --port 8800 //打开报告 host = 本机ip
