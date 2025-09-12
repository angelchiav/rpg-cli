class Player:
    def __init__(self, health=100, money=0, strength=0, defense=0, mana=0, xp=0, level=1):
        self.__health = health
        self.__money = money
        self.__strength = strength
        self.__defense = defense
        self.__mana = mana
        self.__xp = xp
        self.__level = level
        self.__inventory = []

    def get_money(self):
        return self.__money
    
    def get_strength(self):
        return self.__strength
    
    def get_defense(self):
        return self.__defense
    
    def get_mana(self):
        return self.__mana
    
    def get_inventory(self):
        return self.__inventory
    
    def get_xp(self):
        return self.__xp
    
    def set_money(self, value):
        if value < 0:
            raise Exception("Negative money value is not allowed")
        self.__money += value

    def set_strength(self, value):
        if value < 0:
            raise Exception("Negative value is not allowed")
        self.__strength += value
    
    def set_defense(self, value):
        if value < 0:
            raise Exception("Negative value is not allowed")
        self.__defense += value

    def set_mana(self, value):
        if value < 0:
            raise Exception("Negative value is not allowed")
        self.__defense += value
    
    def set_xp(self, value):
        self.__xp = self.__xp - value
        if self.__xp < 0:
            raise Exception("You can't have negative experience")
    
    def set_inventory(self, item):
        if item not in self.__inventory:
            raise Exception("You already have this item")
        self.__inventory.append(item)
        print(f"YOUR INVENTORY:\n {self.__inventory}")

    def delete_from_inventory(self, item):
        if item not in self.__inventory:
            raise Exception("This item is not in the inventory")
        self.__inventory.pop(item)
    
    def kill(self):
        if self.__health <= 0:
            print("You are dead.")

    def set_damage(self, value):
        if self.__health - value > 0:
            print(f"You were hit with {value} points of damage.  Your total health {self.__health}")
        else:
            self.kill()

    def level_up(self):
        self.__level += 1
    
    def become_warrior(self):
        self.__health = 100
        self.__money = 0
        self.__strength = 10
        self.__defense = 8
        self.__mana = 2
        self.__xp = 0
        self.__inventory = ['WOODEN SWORD']

    def become_archer(self):
        self.__health = 80
        self.__money = 0
        self.__strength = 8
        self.__defense = 6
        self.__mana = 7
        self.__xp = 0
        self.__inventory = ['WOODEN ARCH']
    
    def become_wizard(self):
        self.__health = 100
        self.__money = 0
        self.__strength = 4
        self.__defense = 8
        self.__mana = 15
        self.__xp = 0
        self.__inventory = ['WOODEN WAND']
    