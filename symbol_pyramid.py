symbol = input("Enter a symbol ")
n = int(input("enter an odd number "))
# def print_pyramid(symbol, n):
for i in range(n, -1, -1):
    print(' ' * (n - i - 1) + symbol * (2 * i + 1))


# print_pyramid(symbol,n)
# NumberofRows = int(input('Enter the number of rows '))
# NumberofColumns = int(input('Enter the number of columns '))
# Symbols = input('Enter a symbol ')
# for row in range(0, NumberofRows):
#      for column in range(0, NumberofColumns):
#         print('      ' +  Symbols, end='')
#      print('\n')