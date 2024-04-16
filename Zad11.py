def find_max_min_diff(lista):
    if not lista:
        return None
    max_val = max(lista)
    min_val = min(lista)
    return max_val - min_val

liczby = [10, 5, 8, 3, 12]
diff = find_max_min_diff(liczby)
print("Roznica: ", diff)