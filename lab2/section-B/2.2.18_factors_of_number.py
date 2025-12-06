
n = int(input("Enter your number: "))

print(f"Following are the factors of {n}: ")
for i in range(1,int(n**0.5)+1):
    if(n%i == 0):
        print(f"{i} {n//i}",end=" ")

