def make_multiplier(x):
    def mnoznik(n):
        return x * n

    return mnoznik


double = make_multiplier(2)

print(double(5))