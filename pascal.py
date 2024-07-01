# def print_pascal(n):
#     triangle = [[1 for _ in range(i + 1)] for i in range(n)]

#     for i in range(2,n):
#         for j in range(1,i):
#             triangle[i][j] = triangle[i - 1][j-1] + triangle[i -1][j]
#     for row in triangle:
#         print(' '.join(str(num)) for num in row)

def print_pascal(n):
    for line in range(1, n+1):
        C = 1
        for i in range(1, line+1):
            print( "  " * (n - line - 1), C, end = " ")
            C = int (C * (line - i) / i)
        print("  " * (n - line - 1))
n = int(input('Enter the number of rows: '))

print_pascal(n)