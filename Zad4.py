def remove_duplicates(lista):
    seen = set()
    result = []
    for i in lista:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result

liczby = [1,2,3,3,3,4,4,5,6,7,7,8,9]
unikalne = remove_duplicates(liczby)
print(unikalne)