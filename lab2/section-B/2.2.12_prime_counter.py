start = int(input("Start: "))
end = int(input("End: "))

count = 0

for num in range(start,end+1):
    if num<2:
        continue

    is_prime = True
    for i in range(2,int(num**0.5)+1): #searching for divisors expect 1
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        count += 1

print("Total prime numbers =", count)
