def analiza(data):
     match data:
         case []:
             print("Pusta lista")
         case ():
             print("Pusta krotka")
         case [x]:
             print(f"Lista z jednym elementem {x}")
         case [x,y]:
             print(f"Lista z dwoma elemntami {x} i {y}")
         case [x,y,*rest]:
             print(f"lista z conajmniej dwoma elemntami {x} i {y}, {rest}")
         case (x,):
             print(f"Krotka z jednym elementem {x}")
         case (x, y):
             print(f"Krotka z dwoma elemntami {x} i {y}")
         case (x, y, *rest):
             print(f"krotka z conajmniej dwoma elemntami {x} i {y}, {rest}")
         case _:
             print("Ani lista ani krotka")

analiza([])
analiza((3,))
analiza((3,5))
analiza((3,5,6,3))
analiza([2])
analiza([2,5])
analiza([2,5,6,7])
analiza({})