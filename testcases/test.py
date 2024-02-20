import pytest
import requests
from common.logger import logger
from api.pet_V2 import work
from api.pet_V2 import item


def test_function_one(make_request_header):
    # 在测试函数中直接调用 make_request，无需传入 headers
    response = make_request_header(work.work_info)
    # 进行断言等其他操作
    assert response.status_code == 200
    assert response.json().get("code") == "SUCCESS"




def test_item_use(make_request_header):
    logger.info("*************** 开始执行用例 ***************")
    testdata = {"class":2,"item_id":302}
    response = make_request_header(item.item_use, json=testdata)
    assert response.status_code == 200
    # assert result.success == except_code, result.error
    # logger.info("code ==>> 期望结果：{}， 实际结果：{}".format(except_code, result.response.json().get("code")))
    assert response.json().get("code") == "SUCCESS"
    logger.info("*************** 结束执行用例 ***************")


if __name__ == "__main__":
    pytest.main(["-q", "-s", "test.py"])
