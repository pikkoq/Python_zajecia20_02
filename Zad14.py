def count_unique_elements(lista):
    return len(set(lista))

liczby = [1, 2, 2, 3, 4, 4, 5]
unikalne = count_unique_elements(liczby)
print("Liczba unikalnych: ", unikalne)