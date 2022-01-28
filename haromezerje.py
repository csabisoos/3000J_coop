class Tanulo:
    lista = []
    def __init__(self, tanulokod, nev, micsop, acsop, mnyelv, nem, egyuttlakok, testverszam):
        self.tanulokod = tanulokod
        self.nev = nev
        self.micsop = micsop
        self.acsop = acsop
        self.mnyelv = mnyelv
        self.nem = nem
        self.egyuttlakok = egyuttlakok
        self.testverszama = testverszam
        Tanulo.lista.append(self)
        

with open("input.txt", "r", encoding="utf8") as f:
    for sor in f:
        s = sor.strip().split(";")
        t = Tanulo(int(s[0]), s[1], s[2], s[3], s[4], s[5], int(s[6]), int(s[7]))

"""for t in Tanulo.lista:
    print(t.nev)

print(len(Tanulo.lista))
"""


"""
# lambda összehasonlitasa
from parosak import feladat_2_lambda, feladat_2

print(feladat_2_lambda(Tanulo.lista))
print(feladat_2(Tanulo.lista))

"""