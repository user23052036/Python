import os
import math
import random


def factorial(num):

    num = int(num)
    if(num == 0): return 1
    else:
        temp=1.0
        for i in range(1,num+1): temp *= i
        return temp


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

            case "!":
                if(num<0):
                    print("Factorial of negative number not possible")
                    continue
                result = factorial(num)
            
            case "random":
                print(f"random numbers between 1 and {num} is {random.randint(1,int(num))}")

        print(operation, num, " = ", result)

    else:
        # Normal 2-number operations
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        match operation:
            case "+": result = num1 + num2

            case "-": result = num1 - num2

            case "*": result = num1 * num2

            case "/":
                if num2 == 0:
                    print("Division not possible")
                    continue
                result = num1 / num2

            case "^": result = num1 ** num2

            case "%":
                if num2 == 0:
                    print("Division not possible")
                    continue
                result = num1 % num2

            case _:
                print("Invalid operation")
                continue

        print(num1, operation, num2, " = ", result)

    choice = input("Do you want to continue(yes/no): ")
    if choice.lower() not in ["y", "yes"]:
        print("Exiting calculator program")
        break