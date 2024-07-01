user_input = int(input('Enter a number for your factorial '))
def factorial(n):
    if n<0:
        return None
    if n< 2:
        return 1
    product = 1
    for i in range(2, n+1):
        product = product * i
    return product

print(factorial(user_input))