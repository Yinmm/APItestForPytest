import os
# from common.handle_sign import data
import yaml

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def get_data(yaml_file_name):
    data_file_path = os.path.join(BASE_PATH, "data", yaml_file_name)
    with open(data_file_path, encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f)
    return yaml_data

base_data = get_data("base_data.yml")


def set_header(token, md5, t, n, version=base_data["version"]) -> dict:
    header = {
        "Content-Type": "application/json",
        "token": token,
        "Check - Nonce": n,
        "Check - Sign": md5,
        "Check - Time": t,
        "Protocol - Version": version

    }
    return header


print(set_header(1,1,1,1))