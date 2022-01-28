#1) Hány diák tanul az osztályban?

def feladat_1(lista):
    return len(lista)

# 3) Hány lány tanul az osztályban?

def feladat_3(lista):
    i = 0
    for d in lista:
        if d.nem == "lány":
            i += 1
    return i
