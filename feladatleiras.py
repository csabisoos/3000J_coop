"""Az input fájl egy osztály névsorát, különböző tanulócsoportokba történő beosztását és
néhány egyéb adatát tartalmazza. Az egyes adatelemeket pontosvessző választja el. 

Az egyes oszlopok jelentése a következő:
   - tanulokod(szám)
   - diákok neve (szöveg)
   - matematika és informatika szerinti csoportbeosztás (szöveg)
   - angol csoportok szerinti besorolás, a szint és tanár megjelölésével (szöveg)
   - választott 2. idegen nyelv (szöveg)
   - a diák neme, testnevelés szerinti bontás (szöveg)
   - a családban együttlakók száma (szám)
   - testvérek száma (szám)

1) Hány diák tanul az osztályban?
2) Hány fiú tanul az osztályban?
3) Hány lány tanul az osztályban?
4) Hány olyan diák van, akiknek több mint 1 testvére van!
5) Gyűjtse ki azon diákok nevét, akiknek több mint 1 testvérük van!
6) Hány olyan diák van, akiknek több mint 2 testvére van!
7) Gyűjtse ki azon diákok nevét, akiknek több mint 2 testvérük van!
8) Hány olyan diák van, akik a 2. idegen nyelvként a németet tanulják!
9) Gyűjtse ki azon fiú diákok nevét, akik a 2. idegen nyelvként a németet tanulják!
10) Hány diák tanul, az egyes angol csoportban?
11) Hány diák tanul, a kettes angol csoportban?
12) Hány diák tanul, az alfa matematika csoportban?
13) Hány diák tanul, az beta matematika csoportban?
14) Hány lány diák tanul, az alfa matematika csoportban?
15) Hány lány diák tanul, a beta matematika csoportban?
16) Hány fiú diák tanul, az alfa matematika csoportban?
17) Hány fiú diák tanul, a beta matematika csoportban?
18) Van-e olyan diák, aki a 2. idegen nyelvként oroszt tanul?
19) Van-e olyan diák, aki a 2. idegen nyelvként olaszt tanul?
20) Van-e olyan diák, aki a 2. idegen nyelvként spanyolt tanul?
21) Mekkora a legnagyobb család az osztályban?
22) Írjuk ki az egyik olyan diák nevét akinek e legtöbb testvére van!
23) Gyűjtse ki azon lány diákok nevét, akik az egyes vagy kettes angol csoportban vannak!
24) Gyűjtse ki azon fiú diákok nevét, akik a hármas vagy négyes angol csoportban vannak 
    és 0 vagy 2 testvérük van!
25) Viszonylag kevés azon családok száma, ahol az együttlakók száma és a testvérek száma
    között nem három a különbség. Adja meg a számukat!
26) Dári Dóra hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg
    azon tanulók nevét, akik vele azonos angol csoportba járnak.
27) Avon Mór hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg
    azon tanulók nevét, akik vele azonos angol csoportba járnak. 
28) Zúz Mara hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg
    azon tanulók nevét, akik vele azonos angol csoportba járnak. 
29) Citad Ella hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg
    azon tanulók nevét, akik vele azonos angol csoportba járnak. 
30) Hát Izsák hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg
    azon tanulók nevét, akik vele azonos angol csoportba járnak.
31) A spanyol vagy a német nyelvet tanulják-e többben az osztáyban?
32) Kérjen be a felhasználótól egy nyelvet és írja ki, az adott nyelvet tanulók névsorát!
"""