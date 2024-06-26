class Fighter:
    health = 1000 
    def punch(self, opponent):
        opponent.health -= 50
        

        
        

class Boast:
    strength = 100
    def __init__(self):
        print("UNU")
    def boast(self):
        print("You can't see me")
        
    def add(x):
        x.strength += 50
        print("Hellow")
    
    
    
class StrongFighter(Fighter, Boast):
    def kick(self, opponent):
        opponent.health -= 150
        
class MagicFighter(StrongFighter):
    def fireball(self, opponent):
        opponent.health -= 500

class SuperFighter(MagicFighter):
    def punch(self, opponent):
        self.health += 50
        #opponent.health -= 100
        super().punch(opponent)
        
    def fireball(self, opponent):
        self.health += 100
        opponent.health -= 400
        #super().fireball(opponent)
        

fighter1 = Fighter()
fighter2 = MagicFighter()
fighter3 = StrongFighter()
fighter4 = SuperFighter()


def healths():
    print("-------Healths------")
    print(fighter1.health, fighter2.health, fighter3.health, fighter4.health)
    
    
healths()

fighter1.punch(fighter2)
fighter1.punch(fighter2)
fighter1.punch(fighter2)
fighter1.punch(fighter2)

healths()

fighter3.punch(fighter1)
fighter3.kick(fighter2)

fighter2.punch(fighter3)

fighter3.boast()

fighter2.fireball(fighter3)

healths()

fighter4.punch(fighter2)
fighter4.punch(fighter1)

fighter4.fireball(fighter1)

healths()


bh = Boast()

print(bh.strength)
bh.add()
print(bh.strength)