"""paros szamu feladatok megoldasai"""
def feladat_2(lista):
    fiuk = 0
    for tanulo in lista:
        if tanulo.nem == "F":
            fiuk += 1
    return fiuk

def feladat_4(lista):
    x = 0
    for elem in lista:
        if elem.testverszama > 1:
            x += 1
    return x


