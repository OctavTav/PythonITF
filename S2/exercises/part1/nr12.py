"""
12. Ne imaginăm o echipă de fotbal pt teren sintetic.

3 Schimbări maxime admise:

●	Declară o Listă cu 5 jucători

●	Schimbari_efectuate = te joci tu cu valori diferite

●	Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție

-	Efectuează schimbarea

-	Șterge jucătorul scos din listă

-	Adaugă jucătorul intrat

-	Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:

-	Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’

-	Afișază ‘mai ai z schimbări’

"""
jucatori_echipa = ['Momaie', 'Gogaie', 'Gheothe', 'Arthur', 'Maria']
SCHIMBARI_MAX = 3
schimbari_efectuate = 0

print("Pe teren se afla urmatorii: ")
for i in jucatori_echipa:
    print(i, end=" ")
print()

while True:
    schimbare = input("Ce jucator vrei sa inlocuiesti?: ")
    if schimbare in jucatori_echipa:
        #        print(schimbare)
        index_schimbare = jucatori_echipa.index(schimbare)
        if schimbari_efectuate < SCHIMBARI_MAX:
            #            print(schimbari_efectuate)
            #            print(SCHIMBARI_MAX)
            jucatori_echipa.pop(index_schimbare)
            inlocuitor = input("Ce jucator va intra in loc?: ")
            #            print(inlocuitor)
            jucatori_echipa.append(inlocuitor)
            schimbari_efectuate += 1
        else:
            print(f'Ai depasit numarul maxim de schimbari si anume {SCHIMBARI_MAX}')
            break
    else:
        print("Jucatorul nu este in teren")

    raspuns_user = input("Vrei sa mai incerci? Da/Nu ")
    if raspuns_user.lower == "nu":
        break
