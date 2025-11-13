#decimal values are called float, +ve or -ve values are Int, text are strings, true/false are boolean

number = -80 #Int
weight = 65.83 #Float
greeting = "Hello" #String
is_active = True #Boolean
financials = None #None


print(number)
print(weight)
print(greeting)
print("Is user active", is_active)


#Data structures - Multiiple values stored in one variable
#types - list e.g below
cars = ["Audi",
        "Mercedes",
        "Bentley",
        "Nissan"
        ] #In a list, the elemets are ordered and changeable
#You can access one using their position "Index position" which starts from 0 not 1
print(cars)

#Tuple
fruits = ("Apple","Mango") #Ordered and unchangeable
print(fruits)
#Set - Unordered and unchangeable
countries = {"Kenya",
             "Uganda",
             "Italy",
             "USA",
             "Portugal"
             }

#Dictionary
students = {"name": "Alfonce",
            "age": 23,
            "height": "180cm",
            "course": "web development",
            "school": "eMobilis"
            }

#Python strings

x = 'Welcome'
print(x[3]) #The output is "c" since it's the 4th character on indexing 0 1 2 3/W e l c
print(x[3:5])
print(x.upper())

z = "Welcome"
y = "Coders"
print(x,y)
print(countries)
print(students["course"])

#Array - created the same way as a list but has similar data types (strings/int)
languages = ["Python", "PHP", "Java"]
