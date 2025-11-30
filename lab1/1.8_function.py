# Function is a block of code that can be reused in a Program

def factorial_value(num):
  factorial = 1

  if num == 0:
    return factorial

  else:
    for i in range(1, num+1):
      factorial = factorial*i
    return factorial

num1 = int(input("Enter your number for factorial calc: "))
print("factorial of ",num1," is = ",factorial_value(num1))