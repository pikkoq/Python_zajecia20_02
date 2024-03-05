import time

def timeit(funkcja):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = funkcja(*args, **kwargs)
        end = time.time()
        print(f"Funkcja {funkcja.__name__} zrobiona w: {end - start} sekund.")
        return result

    return wrapper


@timeit
def przyklad(liczba):
    total = sum((x for x in range(0, liczba**2)))
    return total

przyklad(5)
przyklad(55)
przyklad(555)
przyklad(5555)
