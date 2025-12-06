

a = int(input("first number: "))
b = int(input("second number: "))

temp_a = a
temp_b = b

while (temp_b != 0):
    temp_a,temp_b = temp_b,temp_a%temp_b

print("LCM =", (a*b)//temp_a)