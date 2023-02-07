import pytest
import allure
from operation.cloth import *
from operation.gm import *
from common.logger import logger
from testcases.conftest import pet_data, get_pet_config


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("服装模块")
class TestCloth(object):
    """衣服模块"""

    @allure.story("用例--服装穿戴保存")
    @allure.description("该用例是服装穿戴保存的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("is_clean_cloth, cloth_list, cloth_save_list, except_code, except_msg",
                             pet_data["test_cloth_save"])
    def test_cloth_save(self, pet_login_hasrole_fixture, is_clean_cloth, cloth_list, cloth_save_list, except_code,
                        except_msg):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        item_list_cloth = get_pet_config.get_ClothesItemConfig()
        token = pet_info["data"]["token"]
        save_dict = {}
        value = 999
        for i in cloth_save_list:
            for j in item_list_cloth:
                if i == j["Type"]:
                    if value == j["ID"]:
                        save_dict[i] = value
                    else:
                        save_dict[i] = j["ID"]
                    break
                if i == value:
                    save_dict["20"] = value  # 物品不存在的验证
                    break

        gm = GM(token)
        if is_clean_cloth == 1:
            gm.gm_clean_cloth()
        set_cloth_list = []
        for i in cloth_list:
            for j in item_list_cloth:
                if i == j["Type"]:
                    set_cloth_list.append(j["ID"])
                    break
        gm.gm_get_cloth(set_cloth_list)
        gm.moditem_list()
        result = cloth_save(token, save_dict)
        assert result.response.status_code == 200
        # assert result.success == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        # assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")

    @allure.story("用例--套装穿戴保存")
    @allure.description("该用例是套装穿戴保存的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("is_clean_cloth, cloth_list, exclude_list, cloth_save_list, except_code, except_msg",
                             pet_data["test_cloth_save_suit"])
    def test_cloth_save_suit(self, pet_login_hasrole_fixture, is_clean_cloth, cloth_list, exclude_list, cloth_save_list,
                             except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        item_list_cloth = get_pet_config.get_ClothesItemConfig()
        token = pet_info["data"]["token"]
        save_dict = {}
        set_cloth_list = []
        if exclude_list == []:
            exclude_list = None
        for i in cloth_save_list:
            for j in item_list_cloth:
                if i == j["Type"]:
                    if i == 20:
                        if exclude_list == j["SuitContain"]:
                            save_dict[i] = j["ID"]
                            set_cloth_list.append(j["ID"])
                            break
                        continue
                    save_dict[i] = j["ID"]
                    set_cloth_list.append(j["ID"])
                    break

        gm = GM(token)
        if is_clean_cloth == 1:
            gm.gm_clean_cloth()
        gm.gm_get_cloth(set_cloth_list)
        gm.moditem_list()
        result = cloth_save(token, save_dict)
        assert result.response.status_code == 200
        # assert result.success == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
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
