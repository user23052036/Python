# A perfect number is a positive integer that is equal to the sum of its proper divisors
# (proper divisors = all divisors except the number itself).

n = int(input("Enter a number: "))

total = 1  # 1 is always a divisor

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        total += i
        other = n // i  # the other divisor
        if other != i:
            total += other

if total == n and n != 1:
    print("Perfect Number")
else:
    print("Not a Perfect Number")


# some examples of perfect number : 6,28,496,8128
# 1 is not a perfect number
