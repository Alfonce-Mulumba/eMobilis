#While loop -Steps to print values in a given range: initialisation, condition setting, & increment or decrement

#Program 1 - increasing
#Initialisation
number = int((input("Enter a number :")))

#Condition set based on the range
while number <= 25:
    print(number)
    number += 1  #Increment

#Program 2
#Decreasing values
count = 500
while count >= 0:
    print("Number is :", count)
    count -= 100   #Decrement


#For Loop
for x in range(40, 51):
    print(x)


#Assignment - a simple program that demonstrates a break & continue statement
#Continue - skips the iterarion to the next
for i in range(1, 11):
    if i == 5:
        continue  # Skip to the next iteration
    print(i)

#Break - stops the count
for i in range(1, 11):
    if i == 5:
        break  # Exit the loop completely
    print(i)
