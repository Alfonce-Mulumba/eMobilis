class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

#Creating objects out of the above class
dog1 = Dog("Umau", "German Shepherd", 3)
dog2 = Dog("Maui", "Local Breed", 5)
dog3 = Dog("Bob", "Chihuahua", 2)

print(dog1.name, dog1.breed, dog1.age)
print(dog2.name, dog2.breed, dog2.age)
print(dog3.name, dog3.breed, dog3.age)