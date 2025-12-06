
a = int(input("first number: "))
b = int(input("second number: "))

while (b != 0):
    a,b = b,a%b    # euclidian gcd

print("GCD =", a)