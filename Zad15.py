def custom_sort(lisa,klucz):
    return sorted(lisa, key=klucz)

slowa = ["jeden", "dwa", "trzy", "czterty", "piec"]
posortowane = custom_sort(slowa, klucz=lambda x: len(x))
print(posortowane)