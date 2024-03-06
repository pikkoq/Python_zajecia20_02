def generator(n):
    for i in range(n):
        yield i * 2

leniwy_generator = generator(5)
for x in leniwy_generator:
    print(x)