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
        if szo[0] != szolanc[-1][-1]:  # Az első betű nem egyezik az előző szó utolsó betűjével
            print("Nem illeszkedett!")
            break

    szolanc.append(szo)  # Ha megfelel, hozzáadjuk a szavak listájához
    szamlalo += 1

print(f"\nHelyes lépések száma: {szamlalo}")

if 0 <= szamlalo <= 2:
    print("Szint: kezdő")
elif 3 <= szamlalo <= 5:
    print("Szint: közepes")
elif 6 <= szamlalo:
    print("Szint: haladó")