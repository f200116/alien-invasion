import json


class GameStats:
    """跟踪游戏的统计信息。"""

    def __init__(self, ai_game):
        """初始化统计信息。"""
        self.settings = ai_game.settings
        self.reset_stats()
        # 任何情况下都不应该重置最高分。
        # 初始化最高分
        self.high_score = 0
        self.update_high_score('init')

        # 游戏启动时处于非活动状态。
        self.game_active = False

        # 游戏启动时处于未暂停状态。
        self.game_pausing = False

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息。"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1


    def update_high_score(self, flag):
        """更新或者初始化最高分
        flag: init or update
        """
        try:
            with open('score.json', 'r') as fr:
                info = json.load(fr)
            if flag == 'init':
                self.high_score = info['high_score']
            elif flag == 'update':
                if self.high_score >= info['high_score']:
                    raise 0

        except:
            if flag == 'init':
                self.high_score = 0
            with open('score.json', 'w', encoding='utf-8') as fw:
                json.dump({"high_score": self.high_score}, fw)


