macierz = [[(i*3) + j + 1 for j in range(3)] for i in range(3)]
for row in macierz:
    print(*row)
