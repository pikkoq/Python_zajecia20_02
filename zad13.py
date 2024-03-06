def calculate_factorial(x):
    if x == 1:
        return x
    else:
        return x * calculate_factorial(x-1)

print(calculate_factorial(6))