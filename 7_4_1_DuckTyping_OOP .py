class Duck:
    def sound(self):
        print("DUCK!!!")
        
class AnotherBrid:
    def sound(self):
        print("Similar to DUCK!")
        
def makeSound(duck):
    duck.sound()


duck = Duck()
duck2 = AnotherBrid()

makeSound(duck)
makeSound(duck2)



