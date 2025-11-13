#The process of a child class acquiring the members (Attributes & Behaviours) of a parent class


class Animal:   #Parent/super/base class
    isMammal = True

    def sound(self):
        print("Animal is making a sound")

class Duck(Animal):  #Child/Sub/Derived class
    hasFeathers = True

    def swim(self):
        print("The Duck is swimming")


class Horse(Animal):
    isWild = True

    def movement(self):
        print("The Horse is galloping")


#Creating objects
a = Animal()
b = Duck()
c = Horse()
