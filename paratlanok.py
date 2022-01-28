#1) Hány diák tanul az osztályban?
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