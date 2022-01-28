#1) Hány diák tanul az osztályban?
from cgitb import reset


def feladat_1(lista):
    return len(lista)

# 3) Hány lány tanul az osztályban?

def feladat_3(lista):
    result = 0
    for d in lista:
        if d.nem == "lány":
            result += 1
    return result

# 5) Gyűjtse ki azon diákok nevét, akiknek több mint 1 testvérük van!

def feladat_5(lista):
    result = []
    for d in lista:
        if d.testverszama < 1:
            result.append(d.nev)
    return result

# 7) Gyűjtse ki azon diákok nevét, akiknek több mint 2 testvérük van!

def feladat_7(lista):
    result = []
    for d in lista:
        if d.testverszama < 2:
            result.append(d.nev)
    return result

# 9) Gyűjtse ki azon fiú diákok nevét, akik a 2. idegen nyelvként a németet tanulják!

def feladat_9(lista):
    result = []
    for d in lista:
        if d.nem == "fiú" and d.mnyelv == "német":
            result.append(d.nev)
    return result

# 11) Hány diák tanul, a kettes angol csoportban?

def feladat_11(lista):
    result = 0
    for d in lista:
        if d.acsop.split('.')[0] == 2:
            result +=1
    return result

# 13) Hány diák tanul, az beta matematika csoportban?

def feladat_13(lista):
    result = 0
    for d in lista:
        if d.micsop == "beta":
            result += 1
    return result

# 15) Hány lány diák tanul, a beta matematika csoportban?

def feladat_15(lista):
    result = 0
    for d in lista:
        if d.nem == "lány" and d.micsop == "beta" :
            result += 1
    return result
    