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

    # Todo sign加密方法

    def to_sign(self):
        key = get_key(self.token, String2arr(self.random), self.aid)
        t = get_current_time()
        result = self.body + t + self.uuid + key + self.version
        sign = hashlib.md5(result.encode()).hexdigest()
        return sign, self.uuid, t

# def to_sign(random, token, tt, aid, body, version, uuid):
#     key = get_key(token, String2arr(random), aid)
#     t = str(tt)
#     result = body + t + uuid + key + str(version)
#     sign = hashlib.md5(result.encode()).hexdigest()
#     print(sign)
#
# random = "4177"
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDg5MzM4NDcsImp0aSI6IjY1ZDMwODU3N2MwNzA5ZWY1YjhiNmNkNSIsImFpZCI6IjY1YjI1NDc3YzIyMTRiZTA1N2U5ODhiMSIsInNlY3VyaXR5X2tleSI6NDE3N30.enCBrx38nEsJiCfRzNCfs4rxI5Xjg0OSSTMfcB-UjiQ"
# tt = "1708329659"
# aid = "65b25477c2214be057e988b1"
# body = None
# md5 = "074aa9d4a1258eb94f11b0500c8d557c"
# version = 19
# uuid = "4c882b45-0724-4ca3-96c7-50cd0f94f794"
# to_sign(random, token, tt, aid, body, version, uuid)

