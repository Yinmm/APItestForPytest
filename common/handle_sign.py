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
        self.version = str(version)response = {Response} <Response [200]>
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
# random = "9246"
# token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDc1NTA0NTgsImp0aSI6IjY1YmRlYzdhMTU0MTNmN2FiMWQxYjkwOSIsImFpZCI6IjY1YjI1NjQ3YzIyMTRiZTA1N2U5ODhlYiIsInNlY3VyaXR5X2tleSI6OTI0Nn0.V8FC2JL7xvFB03Lv2R9vpso44cm7nfG1q75bdElPBZw"
# tt = 1706945658
# aid = "65b25647c2214be057e988eb"
# body = """{"number":2,"item_id":2191002,"target_aid":100291583,"class":2}"""
# md5 = "d82cf07e1b95a4601b11d4bd31ab0c94"
# version = 19
# uuid = "0df1ada1-b978-4bf6-9e15-ed1c2d4a8acf"
# print(body)
# to_sign(random, token,tt, aid, body, version, uuid)

print(get_UUID())