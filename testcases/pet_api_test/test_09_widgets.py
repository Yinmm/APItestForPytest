import pytest
import allure
from operation.widgets import *
from common.logger import logger


@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("小组件模块")
class TestWidgets(object):
    """小组件信息模块"""

    @allure.story("用例--小组件获取信息")
    @allure.description("该用例是小组件信息的测试")
    @pytest.mark.single
    @pytest.mark.smoke
    def test_widgets(self, pet_login_hasrole_fixture):
        logger.info("*************** 开始执行用例 ***************")
        pet_info = pet_login_hasrole_fixture
        token = pet_info["data"]["token"]
        result = widgets_update(token)
        # print(result.__dict__)
        assert result.response.status_code == 200
        # assert result.success == except_code, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：{}".format("SUCCESS", result.response.json().get("code")))
        assert result.response.json().get("code") == "SUCCESS"
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
