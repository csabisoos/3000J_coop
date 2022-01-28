"""paros szamu feladatok megoldasai"""
def feladat_2(lista):
    fiuk = 0
    for tanulo in lista:
        if tanulo.nem == "F":
            fiuk += 1
    return fiuk


