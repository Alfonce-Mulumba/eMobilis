age = int(input("Enter age :"))
if age >= 18:
    print("You are qualified to be a voter")

else:
    print("You're not qualified to vote")


#A py program to return the largest number among three numbers

a = int(input("Enter no.1 :"))
b = int(input("Enter no.2 :"))
c = int(input("Enter no.3 :"))

if a > b and a > c:
   print(a, "is the largest number")

elif b > a and b > c:
    print(b, "is the largest number")

else:
    print(c, "is the largest number")
