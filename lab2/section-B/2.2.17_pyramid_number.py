

row = int(input("Enter row number: "))

for i in range(row):
    for j in range((row-1)*2+1):
        if(j >= row-1-i and j <= row-1+i):
            print("*",end="")
        else: print(" ",end="")
    print()