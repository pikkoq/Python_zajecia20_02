def power_function(exponent):
    def power(x):
        return x ** exponent
    return power

square = power_function(2)
cube = power_function(3)
print(f"Kwadrat liczby 5: {square(5)}")
print(f"Sześcian liczby 3: {cube(3)}")
