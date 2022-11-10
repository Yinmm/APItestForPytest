import ast
from common.read_data import data


class PetGlobalConfig():
    def __init__(self):
        lua_xlsx = r"C:\Users\Administrator\Desktop\PetDoc\Config\Excel\LogicConfig\lua_GlobalConfig.xlsx"
        self.pet_global_config = data.load_lua_xlsx(lua_xlsx)

    def to_list(self, data):
        data = data.replace("{", "[")
        data = data.replace("}", "]")
        List = ast.literal_eval(data)
        return List

    def get_HungerConfig(self):
        """
        【饥饿值】饥饿值区间：参数1-最小值，参数2-最大值，参数3-时间间隔(单位：秒)，参数4-减少值
        """
        HungerConfig = self.pet_global_config["HungerConfig"]
        dict = {
            "min": int(HungerConfig[0]),
            "max": int(HungerConfig[1]),
            "time": int(HungerConfig[2]),
            "reduce": int(HungerConfig[3])
        }
        return dict

    def get_CleanConfig(self):
        """
        【清洁值】清洁值区间：参数1-最小值，参数2-最大值，参数3-时间间隔(单位：秒)，参数4-减少值
        """
        CleanConfig = self.pet_global_config["CleanConfig"]
        dict = {
            "min": int(CleanConfig[0]),
            "max": int(CleanConfig[1]),
            "time": int(CleanConfig[2]),
            "reduce": int(CleanConfig[3])
        }
        return dict

    def get_MoodConfig(self):
        """
        【心情值】心情值区间：参数1-最小值，参数2-最大值，参数3-时间间隔(单位：秒)，参数4-减少值
        """
        MoodConfig = self.pet_global_config["MoodConfig"]
        dict = {
            "min": int(MoodConfig[0]),
            "max": int(MoodConfig[1]),
            "time": int(MoodConfig[2]),
            "reduce": int(MoodConfig[3])
        }
        return dict

    def get_HealthConfig(self):
        """
        【健康值】健康值区间：参数1-最小值，参数2-最大值
        【健康值】健康值减少受饥饿，心情和清洁值等于0时控制：参数1-时间间隔(单位：秒)，参数2-1项等于0时扣除值，参数3-2项等于0时扣除值，参数4-3项等于0时扣除值
        """
        HealthConfig = self.pet_global_config["HealthConfig"]
        dict = {
            "min": int(HealthConfig[0]),
            "max": int(HealthConfig[1]),
            "time": int(HealthConfig[2]),
            "reduce_0": int(HealthConfig[3]),
            "reduce_1": int(HealthConfig[4]),
            "reduce_2": int(HealthConfig[5])
        }
        return dict

    def get_WeightUp(self):
        """
       【体重】体重成长：参数1-时间间隔(单位：秒)，参数2-成长体重(单位：g)
        """
        WeightUp = self.pet_global_config["WeightUp"]
        dict = {
            "time": int(WeightUp[0]),
            "value": int(WeightUp[1])
        }
        return dict

    def get_WeightUpMood(self):
        """
       【体重】体重成长受当前心情值区间影响加成：【{心情值1，心情值2，增加百分比}，{心情值3，心情值4，增加百分比}】
        """
        WeightUpMood = self.pet_global_config["WeightUpMood"]
        List = self.to_list(WeightUpMood)
        dictarry = []
        for i in List:
            dict = {}
            dict["rate"] = i[0]
            dict["range"] = i[1]
            dictarry.append(dict)
        return dictarry

    def get_WeightDown(self):
        """
       【体重】体重减少：参数1-时间间隔(单位：秒)，参数2-减少体重(单位：g)
        """
        WeightDown = self.pet_global_config["WeightDown"]
        dict = {
            "time": int(WeightDown[0]),
            "value": int(WeightDown[1])
        }
        return dict

    def get_WeightDownLimit(self):
        """
       【体重】体重减少限制，参数1-最多减少最大体重的百分比，参数2-体重最多减少到的值(单位：g)
        """
        WeightDownLimit = self.pet_global_config["WeightDownLimit"]
        dict = {
            "max_reduce": int(WeightDownLimit[0]),
            "min_value": int(WeightDownLimit[1])
        }
        return dict

    def get_CreateRoleAttribute(self):
        """
       【创角】初始物品(类型，id，数量)，饥饿值，清洁值，心情值，健康值
        """
        CreateRoleAttribute = self.pet_global_config["CreateRoleAttribute"]
        List = self.to_list(CreateRoleAttribute)
        dict = {
            "hunger": List[0][2],
            "clean": List[1][2],
            "mood": List[2][2],
            "health": List[3][2]
        }
        return dict

    def get_WeightRange(self):
        """
       【体重】体重最小值，体重最大值（单位：g）
        """
        WeightRange = self.pet_global_config["WeightRange"]
        dict = {
            "min": WeightRange[0],
            "max": WeightRange[1]
        }
        return dict

    def get_NicknameOwnerChangeFee(self):
        """
       【修改名字花费】修改主人昵称需要的花费(道具大类、道具id、道具数量)
        """
        NicknameOwnerChangeFee = self.pet_global_config["NicknameOwnerChangeFee"]
        dict = {
            "gold": NicknameOwnerChangeFee[2]
        }
        return dict

    def get_NicknamePetChangeFee(self):
        """
       【修改名字花费】修改宠物昵称需要的花费(道具大类、道具id、道具数量)
        """
        NicknamePetChangeFee = self.pet_global_config["NicknamePetChangeFee"]
        dict = {
            "gold": NicknamePetChangeFee[2]
        }
        return dict

    def get_ShitTrigger(self):
        """
       【拉屎】拉屎触发条件（饥饿值＞x）
        """
        ShitTrigger = self.pet_global_config["ShitTrigger"]
        dict = {
            "hunger": int(ShitTrigger)
        }
        return dict

    def get_ShitCD(self):
        """
       【拉屎】拉屎触发条件（饥饿值＞x）
        """
        ShitCD = self.pet_global_config["ShitCD"]
        dict = {
            "ShitCD": int(ShitCD)
        }
        return dict

    def get_ShitValue(self):
        """
       【拉屎】清理每坨屎所得的奖励（类型，id，数量）
        """
        ShitValue = self.pet_global_config["ShitValue"]
        dict = {
            "ShitReward_type": ShitValue[0],
            "ShitReward_id": ShitValue[1],
            "ShitReward_number": ShitValue[2]
        }
        return dict

    def get_JobHuntTime(self):
        """
       找工作时间（秒）
        """
        JobHuntTime = self.pet_global_config["JobHuntTime"]
        dict = {
            "min": JobHuntTime[0],
            "max": JobHuntTime[1],
        }
        return dict

    def get_JobWorkTime(self):
        """
       工作中时间（秒）
        """
        JobWorkTime = self.pet_global_config["JobWorkTime"]
        dict = {
            "min": JobWorkTime[0],
            "max": JobWorkTime[1],
        }
        return dict


get_pet_config = PetGlobalConfig()