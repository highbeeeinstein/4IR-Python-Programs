# a = int(input('Enter the value of a '))
# b = int(input('Enter the value of b '))
# c = int(input('Enter the value of c '))
# x1 = int((-b +complex((b**2 - 4*a*c)**.5)) / 2*a)
# x2 = int((-b -complex((b**2 - 4*a*c)**.5)) / 2*a)
# print('The values of x are ',x1, 'and', x2)

# DataArray = [1,2,3,4]

# DataFile = open("File.txt", 'w')
# for x in range(0, len(DataArray)):
#     DataFile.write(str(DataArray))

my_List = [2,3]
total = 0
while True:
    number = int(input('Enter a number '))
    my_List.append(number)
    if number == -2:
        break
del my_List[-1]
# print(my_List)
for i in range(len(my_List)):
    total = my_List[-1] + my_List[-2] + my_List[-3]
print(total)

# total = 0
# for i in range(5, 3, -1):
#     total -= i
# print(i)