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

# 25) Viszonylag kevés azon családok száma, ahol az együttlakók száma és a testvérek szám között nem három a különbség. Adja meg a számukat!

def feladat_25(lista):
    result = 0
    for d in lista:
        if d.testverszama+3 != d.egyuttlakok:
            result += 1
    return result

# 27) Avon Mór hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. 

def getindexbyname(lista, name):
    for d in lista:
        if d.nev == name:
            return d

def feladat_27(lista):
    result = []
    a = getindexbyname(lista, "Avon Mór")
    for d in lista:
        if d.nev != a.nev and d.acsop == a.acsop:
            result.append(d.nev)
    return result

# 29) Citad Ella hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. 

def feladat_29(lista):
    result = []
    a = getindexbyname(lista, "Citad Ella")
    for d in lista:
        if d.nev != a.nev and d.acsop == a.acsop:
            result.append(d.nev)
    return result