def addition(num1, num2):
    if isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
        return num1+num2
    else:
        return "invalid addition inputs"
    
def subtraction(num1, num2):
    if isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
        return num1-num2
    else:
        return "invalid sbtraction inputs"
    
def multiplication(num1, num2):
    if isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
        return num1*num2
    else:
        return "invalid multiplication inputs"
    
def power(num1, num2):
    if isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
        return num1**num2
    else:
        return "invalid power inputs"
    
def division(num1, num2):
    if isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
        if num2 != 0:
            return num1/num2
        else:
            return "division by 0 not allowed"
    else:
        return "invalid division inputs"
    
def remainder(num1, num2):
    if isinstance(num1, (int,float)) and isinstance(num2, (int,float)):
        if num2 != 0:
            return num1%num2
        else:
            return "division by 0 not allowed"
    else:
        return "invalid inputs entered"
    
def factorial(num):

    if num<0:
        return "Factorial of negative number not possible"
    if not isinstance(num, (int,float)):
        return "not a valid input to find factorial"
    
    if(num == 0): return 1
    else:
        temp=1.0
        for i in range(1,num+1): temp *= i
        return temp
    
def square_root(num):
    if num<0:
        return "sqare root of negative number is not defined"
    
