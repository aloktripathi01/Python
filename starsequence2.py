rows = int(input("Enter the number of rows :"))
for row in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > row:
            print(" ", end=' ')
        else:
            print("*", end=' ')
            num += 1
    print("")