class Settings:
    """储存游戏《外星人入侵》中所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 5
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5  # 子弹最大数量
        self.bullets_super = True  # 是否打开超级子弹 改为True之后子弹可以穿透外星人

        # 外星人设置
        self.fleet_drop_speed = 5

        # 加快游戏节奏的速度。
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # 外星人分数的提高速度。
        self.score_scale = 1.5

        # 音效设置。


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置。"""
        self.ship_speed = 15
        self.bullet_speed = 15
        self.alien_speed = 50

        # fleet_direction为1表示向右，为-1表示向左。
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度和外星人分数。"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
