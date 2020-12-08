def sum_func(num):
    sum = 0
    for i in range(1,6):
        sum += num ** i
    return sum

def prod_func(num):
    prod = 1
    for i in range(1,6):
        prod *= num ** i
    return prod

def mfunc(x):
    if x > 0:
        return sum_func(x)
    else:
        return prod_func(x)

if __name__ == "__main__":
    a = float(input("Введіть а: "))
    b = float(input("Введіть b: "))
    u = mfunc(a) + mfunc(2) + mfunc(b)
    print("U = ", u)