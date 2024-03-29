import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class Account(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Account, self).__init__(api_root_url, **kwargs)

    # 注册
    def register(self, **kwargs):
        return self.post("/account/register", **kwargs)

    # 登录
    def login(self, **kwargs):
        return self.post("/account/login", **kwargs)

    # 获取新token
    def get_new_token(self, **kwargs):
        return self.post("/account/new_token", **kwargs)

    # 实名认证
    def id_card_auth(self, **kwargs):
        return self.post("/account/id_card_auth", **kwargs)


account = Account(api_root_url)


class Role(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Role, self).__init__(api_root_url, **kwargs)

    # 获取初始宠物类型
    def init_type(self, **kwargs):
        return self.post("/pet/init_type", **kwargs)

    # 创建角色
    def create(self, **kwargs):
        return self.post("/pet/create", **kwargs)

    # 获取详情
    def info(self, **kwargs):
        return self.post("/pet/info", **kwargs)

    # 刷新角色信息
    def update(self, **kwargs):
        return self.post("/account/update", **kwargs)

    # 修改宠物名字
    def change_pet_nickname(self, **kwargs):
        return self.post("/pet/change_pet_nickname", **kwargs)

    # 修改主人昵称
    def change_owner_nickname(self, **kwargs):
        return self.post("/pet/change_owner_nickname", **kwargs)


role = Role(api_root_url)


class Work(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Work, self).__init__(api_root_url, **kwargs)

    # 工作状态
    def work_info(self, **kwargs):
        return self.post("/work/info", **kwargs)

    # 开始打工
    def work_start(self, **kwargs):
        return self.post("/work/start", **kwargs)

    # 领取奖励
    def work_reward(self, **kwargs):
        return self.post("/work/reward", **kwargs)

    # 打工召回
    def work_recall(self, **kwargs):
        return self.post("/work/recall", **kwargs)

    # 小游戏系列
    # 游戏大厅
    def lobby(self,  **kwargs):
        return self.post("/job/lobby", **kwargs)

    # 游戏开始
    def game_start(self,  **kwargs):
        return self.post("/job/game_start", **kwargs)

    # 游戏结算
    def game_over(self,  **kwargs):
        return self.post("/job/game_over", **kwargs)

    # 游戏结算—广告翻倍
    def game_over_ad(self,  **kwargs):
        return self.post("/job/game_over_ad", **kwargs)

    # 游戏成就奖励领取
    # TODO 该接口还需要修改
    def achievement_rewards(self,  **kwargs):
        return self.post("/job/achievement_rewards", **kwargs)

    # 排行榜
    def rank(self,  **kwargs):
        return self.post("/job/rank", **kwargs)

    # 排行榜用户点赞
    def rank_like(self,  **kwargs):
        return self.post("/job/rank_like", **kwargs)


work = Work(api_root_url)


class Item(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Item, self).__init__(api_root_url, **kwargs)

    # 购买物品
    def buy(self, **kwargs):
        return self.post("/item/buy", **kwargs)

    # 物品列表
    def item_list(self, **kwargs):
        return self.post("/item/items", **kwargs)

    # 使用物品
    def item_use(self, **kwargs):
        return self.post("/item/use", **kwargs)


item = Item(api_root_url)


class Room(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Room, self).__init__(api_root_url, **kwargs)

    # 获取装修信息
    def room_get(self, **kwargs):
        return self.post("/room/get", **kwargs)

    # 保存装修信息
    def room_save(self, **kwargs):
        return self.post("/room/save", **kwargs)


room = Room(api_root_url)


class Shit(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Shit, self).__init__(api_root_url, **kwargs)

    # 获取屎信息
    def shit_info(self, **kwargs):
        return self.post("/shit/info", **kwargs)

    # 清理屎
    def shit_clean(self, **kwargs):
        return self.post("/shit/clean", **kwargs)


shit = Shit(api_root_url)


class Widgets(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Widgets, self).__init__(api_root_url, **kwargs)

    # 获取信息
    def widget_update(self, **kwargs):
        return self.post("/widgets/update", **kwargs)


widgets = Widgets(api_root_url)


class GM(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(GM, self).__init__(api_root_url, **kwargs)

    # GM
    def gm(self, **kwargs):
        return self.post("/gm/change_item_quantity", **kwargs)

    def gm_list(self, **kwargs):
        return self.post("/gm/change_item_quantity_batch", **kwargs)

    def super_gm(self, **kwargs):
        return self.post("/gm/web_change_item_quantity", **kwargs)


gm = GM(api_root_url)


class Cloth(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Cloth, self).__init__(api_root_url, **kwargs)

    def cloth_save(self, **kwargs):
        return self.post("/pet/clothes_save", **kwargs)


cloth = Cloth(api_root_url)


class LuckyTree(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(LuckyTree, self).__init__(api_root_url, **kwargs)

    def luck_tree_info(self, **kwargs):
        return self.post("/lucky_tree/info", **kwargs)

    def luck_tree_rewards(self, **kwargs):
        return self.post("/lucky_tree/rewards", **kwargs)


LuckyTree = LuckyTree(api_root_url)


