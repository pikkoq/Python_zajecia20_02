def apply_function_to_tuples(tuples, func):
    return [func(*t) for t in tuples]

my_tuples = [(1, 2), (3, 4), (5, 6)]
result = apply_function_to_tuples(my_tuples, lambda x, y: x + y)
print(f"Wynik zastosowania funkcji: {result}")
