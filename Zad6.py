def apply_function_to_elements(lst, func):
    return [func(x) for x in lst]

my_list = [1, 2, 3, 4, 5]
squared_list = apply_function_to_elements(my_list, lambda x: x**2)
print(f"Lista po zastosowaniu funkcji do elementów: {squared_list}")
