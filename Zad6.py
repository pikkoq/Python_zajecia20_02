def safe_function(funkcja):
    def wrapper(*args, **kwargs):
        try:
            res = funkcja(*args,**kwargs)
            return res
        except Exception as e:
            print(f"Wystąpił bład: {e}")
            return None
    return wrapper

@safe_function
def dziel(a,b):
    return a/b

wynik = dziel(10,2)
wynik2 = dziel(10,0)
print(f"Wynik: {wynik}")
print(f"Wynik 2: {wynik2}")