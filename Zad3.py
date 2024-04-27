def filter_dict_by_even_values(d):
    return {key: value for key, value in d.items() if value % 2 == 0}

my_dict = {1: 3, 2: 4, 3: 5, 4: 6}
filtered_dict = filter_dict_by_even_values(my_dict)
print(f"Słownik po filtrowaniu: {filtered_dict}")
