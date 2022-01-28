"""paros szamu feladatok megoldasai"""
def feladat_2(lista):
    fiuk = 0
    for elem in lista:
        if elem.nem == "F":
            fiuk += 1
    return fiuk

def predikatum(tanulo):
    return tanulo.nem=="F"
def feladat_2_lambda(lista):
    # C# LINQ: x => x.nem 
    # Python: lambda x: x.nem 
    # C# LINQ: (x,y) => x<y && x>a 
    # Python: lambda x,y: x<y
    ## C++: [](int x, int y){return x<y;} 
    
    # lista.Where(t=>t.nem=="F").Count()
    return len(list(filter(lambda t: t.nem=="F", lista)))
    return len(list(filter(predikatum, lista)))
    #return lista.Count(t=>t.nem=="F")


def feladat_4(lista):
    x = 0
    for elem in lista:
        if elem.testverszama > 1:
            x += 1
    return x

def feladat_6(lista):
    x = 0
    for elem in lista:
        if elem.testverszama > 2:
            x += 1
    return x

def feladat_8(lista):
    x = 0
    for elem in lista:
        if elem.mnyelv == "német":
            x += 1 
    return x

def feladat_10(lista):
    x = 0
    for elem in lista:
        if elem.acsop[0] == "1.":
            x += 1
    return x

def feladat_12(lista):
    x = 0
    for elem in lista:
        if elem.micsop == "alfa":
            x += 1
    return x

def feladat_14(lista):
    x = 0
    for elem in lista:
        if elem.micsop == "alfa" and elem.nem == "L":
            x += 1
    return x

def feladat_16(lista):
    x = 0
    for elem in lista:
        if elem.micsop == "alfa" and elem.nem == "F":
            x += 1
    return x

def feladat_18(lista):
    for elem in lista:
        if elem.mnyelv == "orosz":
            return True
    return False

def feladat_20(lista):
    for elem in lista:
        if elem.mnyelv == "spanyol":
            return True
    return False

def feladat_22(lista):
    x = ""
    y = 0
    for elem in lista:
        if elem.testverszama > y:
            y = elem.testverszama
            x = elem.nev
    return x

def feladat_24(lista):
    listasd = []
    for elem in lista:
        if elem.nem == "F" and elem.acsop[0] == "3." or "4." and elem.testverszama == 0 or 2:
            listasd.append(elem.nev)
    return listasd

def feladat_26(lista):
    x = ""
    listasd=[]
    for elem in lista:
        if elem.nev == "Dári Dóra":
            x = elem.acsop[0]
    for elem in lista:
        if elem.acsop == x:
            listasd.append(elem.nev)
    return listasd

def feladat_28(lista):
    x = ""
    listasd=[]
    for elem in lista:
        if elem.nev == "Zúz Mara":
            x = elem.acsop[0]
    for elem in lista:
        if elem.acsop == x:
            listasd.append(elem.nev)
    return listasd

def feladat_30(lista):
    x = ""
    listasd=[]
    for elem in lista:
        if elem.nev == "Hát Izsák":
            x = elem.acsop[0]
    for elem in lista:
        if elem.acsop == x:
            listasd.append(elem.nev)
    return listasd

def feladat_32(lista):
    x = input("Kérem adjon meg egy nyelvet és kiírom az adott nyelvet tanulók sorszámát!")
    listasd = []
    for elem in lista:
        if elem.mnyelv == x:
            listasd.append(elem.nev)
    return lista
"""github"""