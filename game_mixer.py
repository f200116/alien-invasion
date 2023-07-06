import os.path

import pygame


class GameMixer:
    """管理游戏音效的类。"""

    def __init__(self, ai_game):
        """初始化mixer属性。"""
        pygame.mixer.init()
        self.kill_mixer = pygame.mixer.Sound(os.path.join("sound", 'kill.wav'))
        self.die_mixer = pygame.mixer.Sound(os.path.join("sound", 'boom.wav'))

    def create_kill_mixer(self):
        """创造击杀外星人声音。"""
        pygame.mixer.Sound.play(self.kill_mixer)

    def create_die_mixer(self):
        """创造飞船被撞的声音。"""
        pygame.mixer.Sound.play(self.die_mixer)
