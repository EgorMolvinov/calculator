import math
from itertools import cycle
import sys
a = float(input("\nFirst number: "))
    
what = input("What are we doing? (+, -, *, /, **, sqrt): ")


if what == "+":
    b = float(input("Second number: "))
    c = a + b
    print ("\nResult: " + str(c))
    print ("\n")
    

elif what == "-":
    b = float(input("Second number: "))
    c = a - b
    print ("\nResult: " + str(c))
    print ("\n")
    
elif what == "*":
    b = float(input("Second number: "))
    c = a * b
    print ("\nResult: " + str(c))
    print ("\n")
    
elif what == "/":
    b = float(input("Second number: "))
    c = a / b
    print ("\nResult: " + str(c))
    print ("\n")
    
elif what == "**":
    b = float(input("Second number: "))
    c = a ** b
    print ("\nResult: " + str(c))
    print ("\n")
    
elif what == "sqrt":
    print(a ** 0.5)
    print(pow(a, 0.5))
    print (" \n ")
else:
    print ("Incorrect operation")

repeater = 5
while repeater < 10:
    num = int(input("Press 0 to repeat\nPress 2 to exit  "))
    while num == 2:
        quit()
    while num < 1:
        import math
        from itertools import cycle
        a = float(input("\nFirst number: "))
    
        what = input("What are we doing? (+, -, *, /, **, sqrt): ")


        if what == "+":
            b = float(input("Second number: "))
            c = a + b
            print ("\nResult: " + str(c))
            print ("\n")
    

        elif what == "-":
            b = float(input("Second number: "))
            c = a - b
            print ("\nResult: " + str(c))
            print ("\n")
    
        elif what == "*":
            b = float(input("Second number: "))
            c = a * b
            print ("\nResult: " + str(c))
            print ("\n")
    
        elif what == "/":
            b = float(input("Second number: "))
            c = a / b
            print ("\nResult: " + str(c))
            print ("\n")
    
        elif what == "**":
            b = float(input("Second number: "))
            c = a ** b
            print ("\nResult: " + str(c))
            print ("\n")
    
        elif what == "sqrt":
            print(a ** 0.5)
            print(pow(a, 0.5))
            print (" \n ")
        else:
            print ("Incorrect operation")
        break
