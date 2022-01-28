#1) Hány diák tanul az osztályban?
from cgitb import reset
from unittest import result


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
        if d.acsop.split('.')[0] == '2':
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

# 17) Hány fiú diák tanul, a beta matematika csoportban?

def feladat_17(lista):
    result = 0
    for d in lista:
        if d.nem == "fiú" and d.micsop == "beta" :
            result += 1
    return result

# 19) Van-e olyan diák, aki a 2. idegen nyelvként olaszt tanul?

def feladat_19(lista):
    for d in lista:
        if d.mnyelv == "olasz":
            return True
    return False

# 21) Mekkora a legnagyobb család az osztályban?

def feladat_21(lista):
    result = 0
    for d in lista:
        if result < d.egyuttlakok:
            result = d.egyuttlakok
    return result

# 23) Gyűjtse ki azon lány diákok nevét, akik az egyes vagy kettes angol csoportban vannak!

def feladat_23(lista):
    result = 0
    for d in lista:
        if d.nem == "lány" and d.acsop.split('.') == "1" or d.acsop.split('.') == "2":
            result += 1
    return result