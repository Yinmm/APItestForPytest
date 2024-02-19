import pytest
from common.logger import logger
from api.pet_V2 import work


def test_function_one(make_request):
    # 在测试函数中直接调用 make_request，无需传入 headers
    response = make_request(work.work_info)
    # 进行断言等其他操作
    assert response.status_code == 200
    assert response.json().get("code") == "SUCCESS"
    print(response)


if __name__ == "__main__":
    pytest.main(["-q", "-s", "test.py"])
