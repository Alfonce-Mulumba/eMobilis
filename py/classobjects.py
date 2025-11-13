# OOP - Creating a program within a file using classes and objects (helps avoid repetition for objects with common characteristics)
#A class is a blueprint of an object
#Object - an instance of a class

class Student:
    #Attributes/variables - details of the class
    name = "Alfonce"
    gender = "Male"
    age = 23
    course = "Web Development"

    #Behaviour/Methods/Functions
    def study(self):
        print("Student is studying")



#Creating an object
student1 = Student()  #Object 1
print(student1.name, student1.gender,student1.age, student1.course)

student1.study() #For behaviour, call the method


student2 = Student()  #Object 2

student3 = Student()  #Object 3

