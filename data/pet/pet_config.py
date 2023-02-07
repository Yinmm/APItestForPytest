from common.read_data import data
import os

curPath = os.path.abspath(os.path.dirname(__file__))
config_path = curPath + "/json"


class PetConfig:
    def __init__(self):
        pass

    def get_FinishItemConfig(self) -> list:
        config_json_data = data.load_json(config_path + "/FinishItemConfig.json")["Data"]
        return config_json_data

    def get_GlobalConfig(self) -> list:
        config_json_data = data.load_json(config_path + "/GlobalConfig.json")["Data"]
        return config_json_data

    def get_ClothesItemConfig(self) -> list:
        config_json_data = data.load_json(config_path + "/ClothesItemConfig.json")["Data"]
        return config_json_data


get_pet_config = PetConfig()

