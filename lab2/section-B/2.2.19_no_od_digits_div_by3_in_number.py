n = input()
c = 0

for d in n:
    if(int(d)% 3 == 0): c += 1
print(f"no of off digits in the number {n} = ",c)
