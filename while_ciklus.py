szolanc = []
szamlalo = 0

while True:
    szo = input(f"{szamlalo + 1}. szó: ")
    if szamlalo == 0:
        if len(szo) != 6:   # Első szó esetén nincs ellenőrzés
            print("A karakterek száma téves! ")
            break
    else:
        # Minden további szó esetén ellenőrizni kell a hosszt és az illeszkedést
        if len(szo) != 6:
            print("A karakterek száma téves! ")
            break
        elif szo[0] != szolanc[-1][-1]:  # Az első betű nem egyezik az előző szó utolsó betűjével
            print("Nem illeszkedett!")
            break

    szolanc.append(szo)  # Ha megfelel, hozzáadjuk a szavak listájához
    szamlalo += 1

# Áttekintés:
# A while True: egy végtelen ciklust indít, ami addig fut, amíg valamilyen break utasítás meg nem szakítja.
# Ebben a ciklusban kérünk be szavakat a felhasználótól, ellenőrizzük, hogy megfelelnek-e a szabályoknak, és ha igen,
# hozzáadjuk őket a szólánchoz. Ha bármelyik szabály megsértése történik, a ciklus a break utasítással véget ér.

# Részletes magyarázat
# 1. Szó bekérése:
#
# szo = input(f"{szamlalo + 1}. szó: ")
#
# A program bekéri a felhasználótól a következő szót, és eltárolja a szo változóban.
# A szamlalo + 1 kifejezés a megfelelő sorszámot jeleníti meg a felhasználó számára.

# 2. Első szó ellenőrzése:
#
# if szamlalo == 0:
#     if len(szo) != 6:
#         print("A karakterek száma téves! ")
#         break
#
# Ha ez az első szó (azaz szamlalo == 0), akkor csak azt ellenőrizzük, hogy a szó hossza pontosan hat karakter-e.
# Ha nem, akkor kiírjuk, hogy „A karakterek száma téves!”, és megszakítjuk a ciklust a break utasítással.

# 3. További szavak ellenőrzése
#
# elif len(szo) != 6:
#     print("A karakterek száma téves! ")
#     break
# if szo[0] != szolanc[-1][-1]:  # Az első betű nem egyezik az előző szó utolsó betűjével
#     print("Nem illeszkedett!")
#     break
#
# Ha már volt előző szó (szamlalo != 0), akkor két dolgot ellenőrzünk:
#     1. Szó hossza: Ha a szó nem hat karakterből áll, ugyanúgy megszakítjuk a ciklust, mint az első szó esetében.
#     2. Illeszkedés ellenőrzése: Ha a szó első betűje (szo[0]) nem egyezik meg az előző szó utolsó betűjével
#     (szolanc[-1][-1]), akkor kiírjuk, hogy „Nem illeszkedett!”, és megszakítjuk a ciklust.

# 4. Érvényes szó hozzáadása a listához
#
# szolanc.append(szo)  # Ha megfelel, hozzáadjuk a szavak listájához
# szamlalo += 1
#
# Ha a szó megfelel minden szabálynak, akkor hozzáadjuk a szolanc listához, majd növeljük a szamlalo változót.
# Ez biztosítja, hogy a következő alkalommal a program a megfelelő sorszámmal kérdezzen.

# A ciklus vége
#
# Amikor a break utasítás végrehajtódik (azaz a ciklust megszakítjuk), a program folytatódik a while ciklus után,
# ahol kiírja a helyes lépések számát és a felhasználó szintjét.

# Összefoglalás
#
# A while ciklus lényege tehát, hogy addig ismétlődően kér be szavakat, amíg a felhasználó be nem visz egy szabályellenes
# szót. Minden beolvasott szó után ellenőriz, és ha minden feltétel teljesül, akkor hozzáadja a szót a listához
# és folytatja a következő bevitellel. Ha bármelyik feltétel nem teljesül, a ciklus leáll, és a program kiírja az
# eredményeket.