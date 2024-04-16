def remove_whitespace(lista):
    return [s.strip() for s in lista]

slowa = ["   dawda", "dwada ", "  dawda d dwdwa  "]
wynik = remove_whitespace(slowa)
print(wynik)