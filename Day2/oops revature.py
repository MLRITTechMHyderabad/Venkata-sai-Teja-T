class character:
    def __init__(self,name,health,attack_power,defense,speed):
        self.name=name
        self.health=health
        self.attack_power=attack_power
        self.defense=defense
        self.speed=speed
    def attack(self,target):
        pass
    def take_damage(self,amount):
        pass
    def is_alive(self):
        pass
class warrior(character):
    def __init__(self,rage):
        self.rage=rage
    def berserk_mode(self):
        if self.health<30:
            self.attack_power*=2
teja=character("sai",20,4,2,300)
te=warrior(2)
te.berserk_mode()
print(teja.attack_power)
    
    
