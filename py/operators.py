#Used for calculations
#1. Arithmetic Operators (simple calculations)
x = 34
y = 2
a = "3"
b = "4"


print(x + y,
      x - y,
      x * y,
      x / y,
      x % y) #Modulus - divides the numbers and returns the remainder
print(a + b)

#2. Comparison Operators (Used to compare values) - returns boolean (true/false)
c = 89
d = 56

print(c > d,
      c < d,
      c >= d,
      c <= d,
      c == d,
      c != d   #Not(!) equal to
      )

#3. Assignment Operators "=" - Used to assign values to variables
number = 60
print(number)
number %= 4
print(number)
#Operator precedence - The order in which operations get executed

output = 6 - 2 + 4 * 3
print(output)

#Logical Operators - When you have more than one condition to be set(and, or, not)
print(50 > 16 and 67 > 20 and 56 < 90) #"and" returns "True" if all conditions are true. 
print(30 < 48 and 50 > 60 and 70 < 100) #if any of the conditions is false, "and" returns false
print(50 > 16 or 67 > 20 or 56 < 90) #"or" returns a True if any of the conditions is true
print(not(50 > 16 and 67 > 20 and 56 < 90)) #"not" retuns the opposite of the result


#**************Other Operators*************
#4. Bitwise Operators
#5. Membership Operators