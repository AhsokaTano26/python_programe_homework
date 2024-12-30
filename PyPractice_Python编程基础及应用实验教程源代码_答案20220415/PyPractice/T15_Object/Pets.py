class Pet:
    def __init__(self,name):
        self.__sName = name

    def getName(self):
        return self.__sName

class Rabbit(Pet):
    def __init__(self,name):
        Pet.__init__(self,name)
    
    def speak(self):
        print(f"Hello from rabbit {self.getName()}.")

    def eat(self,iWeight):
        print(f"Rabbit {self.getName()} ate {iWeight} gram's food.")

class Cat(Pet):
    def __init__(self,name):
        Pet.__init__(self,name)

    def eat(self,iWeight):
        print(f"Cat {self.getName()} ate {iWeight} gram's food.")   

class DragonLi(Cat):
    def __init__(self,name):
        Cat.__init__(self,name)

    def speak(self):
        print(f"Hello from dragonli cat {self.getName()}.")

class Persian(Cat):
    def __init__(self,name):
        Cat.__init__(self,name)

    def speak(self):
        print(f"Hello from persian cat {self.getName()}.")

print("-------------Rabbit Charlie--------------")
r = Rabbit("Charlie")
r.eat(100)
r.speak()  

print("-------------Cat Lucy--------------")
c1 = DragonLi("Lucy")
c1.eat(200)
c1.speak()

print("-------------Cat Eddie--------------")
c2 = Persian("Eddie")
c2.eat(100)
c2.speak()

print(isinstance(c1,Persian))
print(isinstance(c1,DragonLi))
print(isinstance(c1,Cat))
print(isinstance(c1,Pet))
print(isinstance(r,Pet))
print(isinstance(r,Rabbit))
print(isinstance(r,Persian))




