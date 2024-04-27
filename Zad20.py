def sum_of_squares_of_odds(numbers):
    return sum(x**2 for x in numbers if x % 2 != 0)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_of_squares_of_odds(my_list)
print(f"Suma kwadratów liczb nieparzystych: {result}")
