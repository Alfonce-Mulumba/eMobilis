#A function is a method (A block of code that performs a task)
# 1. Standard Library Functions/Inbuilt - Already exist


number = max(45, 89, 56, 32, 10)
print("The maximum value is :", number)

x = min(90, 48, 30, 70, 83)
print("The minimum value is :", x)

# 2. User defined functions - created and designed by the user
def greeting():
    print("Hello Alfonce!")

greeting()  #Calling function

#Parameters and arguments
def sub(x, y):  #Parameters
    print("The difference is :", x - y)
sub(int(input("Enter number :")), int(input("Enter number to deduct :"))) #Arguments


def add():
    x = int((input("Enter 1st number :")))
    y = int((input("Enter 2nd number to add :")))
    print("The sum is :", x + y)
add()


