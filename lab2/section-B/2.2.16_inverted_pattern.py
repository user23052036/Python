

row = int(input("Enter no of rows: "))

for i in range(0,row):
    for j in range(0,row-i):
        print("*" ,end="")
    print(end="\n")