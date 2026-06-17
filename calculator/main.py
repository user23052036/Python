import os
import math
import random

import basic_operations


while(True):

    os.system("clear")

    print("Available operations: +  -  *  / sqrt  ^  !  sin  cos  tan random")
    operation = input("Enter operation: ")

     # For trig functions & sqrt, we need only one number
    if operation in ["sin", "cos", "tan", "sqrt","!","random"]:
        num = float(input("Enter the number: "))
        
        # these trig functons take entries in radian so they need type convert
        match operation:
            case "sin": result = math.sin(math.radians(num))

            case "cos": result = math.cos(math.radians(num))

            case "tan": result = math.tan(math.radians(num))

            case "sqrt":
                if(num < 0):
                    print("Square root of negative number not possible")
                    continue
                result = math.sqrt(num)

            case "!": result = basic_operations.factorial(num)
            
            case "random":
                print(f"random numbers between 1 and {num} is {random.randint(1,int(num))}")

        print(operation, num, " = ", result)

    else:
        # Normal 2-number operations
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        match operation:
            case "+": result = basic_operations.addition(num1,num2)
            case "-": result = basic_operations.subtraction(num1,num2)
            case "*": result = basic_operations.multiplication(num1,num2)
            case "/": result = basic_operations.division(num1,num2)
            case "^": result = num1 ** num2
            case "%": result = basic_operations.remainder(num1,num2)
            case _: result = basic_operations.power(num1,num2)

        print(num1, operation, num2, " = ", result)

    choice = input("Do you want to continue(yes/no): ")
    if choice.lower() not in ["y", "yes"]:
        print("Exiting calculator program")
        break