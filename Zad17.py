def capitalize_all_words(string):
    return ' '.join(word.capitalize() for word in string.split())

zdanie = "siema co tam byqu"
wielka = capitalize_all_words(zdanie)
print(wielka)