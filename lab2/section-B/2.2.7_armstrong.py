num = int(input("Enter a number: "))

# convert number to string for digit count
digits = str(num)
power = len(digits)

sum_val = 0
for d in digits:
    sum_val += int(d) ** power

if sum_val == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")




# 2345 = 2^4 + 3^4 + 4^4 + 5^4 ---> armstrong number
