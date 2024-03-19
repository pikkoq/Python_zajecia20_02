lista = [1,2,3,4,5,6,7,8,9,10]

squareList = [x*x for x in lista if (sum := pow(x,2) > 10)]

print(squareList)