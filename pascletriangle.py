def pascal_triangle(n):
    for i in range(n):
         # First number in every row is 1

    num = 1
    for j in range(i + 1):
    print(num, end=" ")
# update valiue using binomial coefficient formula
    num = num * (i - j) // (j + 1)
    print()
# taking input
rows = int(input("Enter number of rows:"))
pascle_triangle(rows)
