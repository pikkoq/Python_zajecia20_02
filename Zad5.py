def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parts = list(chunks(my_list, 2))
print(f"Podzielona lista: {parts}")
