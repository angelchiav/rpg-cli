import random
import player

class Enemy:
    def __init__(self, attack=0, defense=0, xp=0, health=0):
        self.__attack = attack
        self.__defense = defense
        self.__xp = xp
        self.__health = health

    def hit(self, player):
        damage = random.randint(1, self.__attack)
        player.hp -= damage

    def kill(self):
        if self.__health <= 0:
            return

class Goblin(Enemy):
    def __init__(self, attack=2, defense=3, xp=random.randint(1,10), health=10):
        super().__init__(attack, defense, xp, health)