import uuid
import time
import hashlib


def get_UUID():
    return str(uuid.uuid4())


def body2String(body):
    return str(body)


def String2arr(str):
    return list(str)


def get_key(token, arr, aid):
    length = int(arr[0]) + int(arr[1] + arr[2])
    key1 = token[int(arr[0]):length]
    key2 = key1[0:int(arr[3])] + aid + key1[int(arr[3]):]
    return key2


def get_current_time():
    return str(int(time.time()))


class HandleSign:
    def __init__(self, random, token, aid, version, body):
        self.random = str(random)
        self.token = str(token)
        self.aid = str(aid)
        self.uuid = get_UUID()
        self.version = str(version)
        self.body = body2String(body)


    def to_sign(self):
        key = get_key(self.token, String2arr(self.random), self.aid)
        t = get_current_time()
        result = self.body + t + self.uuid + key + self.version
        sign = hashlib.md5(result.encode()).hexdigest()
        return sign, self.uuid, t


def to_test_sign(random, token, tt, aid, body, version, uuid):
    key = get_key(token, String2arr(random), aid)
    t = str(tt)
    result = body + t + uuid + key + str(version)
    sign = hashlib.md5(result.encode()).hexdigest()
    print(sign)


# random = "1106"
# token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDkwMTk3MjQsImp0aSI6IjY1ZDQ1N2NjMWVjMzFjZjI4MmRiMGNlOSIsImFpZCI6IjY1YjI1NDc3YzIyMTRiZTA1N2U5ODhiMSIsInNlY3VyaXR5X2tleSI6MTEwNn0.R0Y94Ch42zNTDtQuz4l9U04BoGC-QZjJr6o2vA2NwsY"
# tt = "1708414923"
# aid = "65b25477c2214be057e988b1"
# body = "{'class': 2, 'item_id': 100}"
# md5 = "6a6f6843b323b573127755d1862e3f05"
# version = 19
# uuid = 'e667b112-f6fa-4175-a2d6-7b00cb8bbb04'
# to_test_sign(random, token, tt, aid, body, version, uuid)

