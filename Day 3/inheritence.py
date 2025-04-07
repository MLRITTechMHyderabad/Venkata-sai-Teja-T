
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
        if self.health<=0:
            print("character is defeated")
class warrior(character):
    def __init__(self,rage,n,h,a,d,s):
        super().__init__(n,h,a,d,s)
        self.rage=rage
    def berserk_mode(self):
        if self.health<30:
            self.attack_power*=2
class maze(character):
    def __init__(self,mana,n,h,a,d,s):
        super().__init__(n,h,a,d,s)
        self.mana=mana
    def fireball(self):
        pass
class archer(character):
    def __init__(self,crirical_chance,n,h,a,d,s):
        super().__init__(n,h,a,d,s)
        self.crirical_chance=crirical_chance
    def precision_shot(self):
        pass

alice=archer(2,"alice",0,22,3,4)
alice.is_alive()

thor=warrior(3,"thor",40,33,4,44)
gandalf=maze(4,"gandalf",5,3,3,4)




    
    
