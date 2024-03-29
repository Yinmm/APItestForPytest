import pytest
import allure
from operation.item import *
from operation.gm import GM
from testcases.conftest import pet_data, pet_config
from common.logger import logger


@allure.step("前置步骤 ==>> 设置数据")
def step_item_use(gold, hunger, heath, clean, mood, Class, ID):
    logger.info(
        "前置步骤===>前置金币数量-{},前置饥饿值-{},前置健康值-{},前置清洁值-{},前置心情值-{},使用物品类别-{},使用物品ID-{},".format(gold, hunger, heath, clean,
                                                                                            mood, Class, ID))


@allure.step("前置步骤 ==>> 设置数据")
def step_item_buy(gold, Class, ID, number):
    logger.info("前置步骤===>前置金币数量-{},购买物品类别-{},购买物品ID-{},购买数量-{}".format(gold, Class, ID, number))


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("物品模块")
class TestItem(object):
    """物品信息模块"""

    @allure.story("用例--获取物品列表")
    @allure.description("该用例是获取宠物工作状态的测试")
    # @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    # @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.single
    @pytest.mark.smoke
    def test_item_list(self, pet_login_hasrole_fixture):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        result = item_list(token)
        # print(result.__dict__)
        assert result.response.status_code == 200
        # assert result.success == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format("SUCCESS", result.response.json().get("code")))
        assert result.response.json().get("code") == "SUCCESS"
        # assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--使用物品")
    @allure.description("该用例是使用物品的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("gold,hunger,heath,clean,mood,Class, ID, except_code, except_msg",
                             pet_data["test_item_use"])
    def test_item_use(self, pet_login_hasrole_fixture, gold, hunger, heath, clean, mood, Class, ID, except_code,
                      except_msg):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        step_item_use(gold, hunger, heath, clean, mood, Class, ID)
        gm = GM(token)
        gm.gm_gold(gold)
        gm.gm_mood(mood)
        gm.gm_clean(clean)
        gm.gm_heath(heath)
        gm.gm_hunger(hunger)
        gm.moditem_list()
        result = item_use(token, Class, ID)
        # print(result.__dict__)
        assert result.response.status_code == 200
        # assert result.success == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--购买物品（仅家具和服装）")
    @allure.description("该用例是购买物品的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("gold, cloth, furniture, Class, ID_type, number, except_code, except_msg",
                             pet_data["test_item_buy"])
    def test_item_buy(self, pet_login_hasrole_fixture, gold, cloth, furniture, Class, ID_type, number, except_code,
                      except_msg):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        item_id = 999
        item_gold = 0
        item_list = pet_config.get_FinishItemConfig()+pet_config.get_ClothesItemConfig()
        if ID_type != item_id:
            for i in item_list:
                if ID_type == i["Type"]:
                    item_id = i["ID"]
                    item_gold = int(gold*int(i["ObtainExpend"]["amount"]))
                    break
        step_item_buy(item_gold, Class, item_id, number)
        gm = GM(token)
        gm.gm_gold(item_gold)
        if cloth == 1:
            gm.gm_clean_cloth()
        if furniture == 1:
            gm.gm_clean_furniture()
        gm.moditem_list()
        result = item_buy(token, Class, item_id, number)
        assert result.response.status_code == 200
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
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
