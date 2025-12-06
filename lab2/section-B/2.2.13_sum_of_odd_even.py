

n = input("Enter your number: ")
odd = even = 0

for d in n:
    if(int(d)%2 == 0): 
        even += int(d)
    else: odd += int(d)
print("Odd sum =", odd, "Even sum =", even)
