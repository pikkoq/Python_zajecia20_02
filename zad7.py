listaSlow = ["Dzien", "Dobry", "Awokado", "Ananas", "Banan"]

def zaczyna(word):
    if len(word) > 5:
        return True
    else:
        return False
slowa = filter(zaczyna,listaSlow)
for x in slowa:
    print(x)