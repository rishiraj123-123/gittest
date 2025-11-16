x=int(input("Enter a number: "))
def factorial(x):
    if 0<x<=1:
        fact=1
    else:
        fact=x*factorial(x-1)
    return fact
print( f'Factorial of {x} is: {factorial(x)}')

