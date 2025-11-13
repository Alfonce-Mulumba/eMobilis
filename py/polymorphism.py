#Many forms of a method (Behaviours)/ same method, different implementations

class Dog:
    def sound(self):
        print("Woof! Woof! Wooh!!")

class Cat:
    def sound(self):
        print("Meoow! Meeooowww!!")


#creating objects out of the class
d = Dog()
d.sound()

c = Cat()
c.sound()
