
n = int(input("Enter number to digits: "))
count = 0
while (n > 0):
    count += 1
    n //= 10     # int division(round of)
print(count)
