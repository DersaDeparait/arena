from GameSystem import Box
from GameSystem import Hero

class User:
    def __init__(self, heroes:list = []):
        self.box = Box()
        self.heroes = heroes

    def add_hero(self, hero: Hero):
        self.heroes.append(hero)
