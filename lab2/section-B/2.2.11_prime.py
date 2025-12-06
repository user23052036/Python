
for n in range(2,101):
    for i in range(2, (int)(n**0.5)+1):  # just need to iterate upto root(n)+1
        if n % i == 0: break
    else:
        print(n)
