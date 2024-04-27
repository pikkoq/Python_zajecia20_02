def sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_of_even_numbers(my_list)
print(f"Suma parzystych liczb: {result}")
