row = int(input("Enter row number: "))
cols = 2*row - 1

for i in range(row):
    for j in range(cols):
        # top tip, left edge, right edge, or bottom row -> star
        if (i == 0 and j == row - 1) or \
           (j == row - i - 1) or \
           (j == row + i - 1) or \
           (i == row - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
