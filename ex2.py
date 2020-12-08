from math import sqrt, sin

def right_square(a, x, func):
    return (x - a) * eval(func)

a = int(input('Введіть а: '))
b = int(input("Введіть b: "))

s = right_square(a, 3, "sqrt((4 * x) + sin(sqrt(x ** 3)))") + right_square(a, b, "sqrt((4 * x) + sin(sqrt(x ** 3)))")
print("S = ", s)