def generate_fibonacci():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b

generator = generate_fibonacci()
for _ in range(15):
    print(next(generator))