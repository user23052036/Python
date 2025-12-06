num = int(input("Enter how many Fibonacci numbers you want: "))

fib_list = []

def fibo(n):
    if n <= 1: return n # base condition
    return fibo(n-1) + fibo(n-2)



for i in range(num):
    fib_list.append(fibo(i))
print(fib_list)