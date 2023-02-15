import os
import yaml, hashlib

filepath = os.path.abspath(os.path.dirname(os.getcwd()))


def get_yaml_data(yaml_file):
    with open(yaml_file, encoding='utf-8') as file:
        content = file.read()
        # 设置Loader=yaml.FullLoader忽略YAMLLoadWarning警告
        data = yaml.load(content, Loader=yaml.FullLoader)
        return data


# 装饰类
def md5_second(func):
    def inner_func():
        text = func()
        hl = hashlib.md5()
        hl.update(text.encode(encoding='utf-8'))
        sec_text = hl.hexdigest().upper()
        print(sec_text)
        with open(filepath + "/CaseData/case_contract_photo_checkShare.yaml", 'r') as f:
            result = yaml.load(f.read(), Loader=yaml.FullLoader)
            result['sign'] = sec_text
            with open(filepath + "/CaseData/case_contract_photo_checkShare.yaml", 'w+') as f:
                yaml.dump(data=result, stream=f, allow_unicode=True)

    return inner_func


@md5_second
def sign():
    filepath = os.path.abspath(os.path.dirname(os.getcwd()))
    data = get_yaml_data(filepath + "/CaseData/case_contract_photo_checkShare.yaml")
    data_dict = data.get('properties')
    # 将参数添加到列表
    L = list()
    for i in data_dict:
        print(i)
        L.append(i)
    # 列表的长度
    n = len(L)
    for i in range(n):
        for j in range(0, n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    # 打印冒泡排序后的列表
    parameters = ''
    for i in L:
        # 判断 是否为sign
        if i == 'sign':
            continue
        else:
            xx = i + '=' + data_dict.get(i)['example']
            parameters += xx
    s_parameters = parameters[::-1]
    print(s_parameters)

    hl = hashlib.md5()
    hl.update(s_parameters.encode(encoding='utf-8'))
    md5_text = hl.hexdigest().upper()
    print(md5_text)
    return md5_text


if __name__ == '__main__':
    sign()
