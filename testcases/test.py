import pytest
from common.logger import logger
from api.pet_V2 import work


def test_function_one(make_request):
    # 在测试函数中直接调用 make_request，无需传入 headers
    response = make_request(work.work_info)
    print(response)


if __name__ == "__main__":
    pytest.main(["-q", "-s", "test.py"])
