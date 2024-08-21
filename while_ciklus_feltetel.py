# Kontextus
# Ez a sor a szólánc játék egyik szabályát ellenőrzi: a következő szó első betűjének egyeznie kell
# az előző szó utolsó betűjével.

# if szo[0] != szolanc[-1][-1]:

# Ez a sor két dolgot hasonlít össze:
#
#     1. szo[0]: Az aktuálisan beírt szó (szo) első karaktere.
#     2. szolanc[-1][-1]: Az előző szó utolsó karaktere a szolanc listában.

# Miért pont így?
#
#     1. szo[0]:
#     A Pythonban a karakterláncok (stringek) indexelhetők, ami azt jelenti, hogy elérheted bármelyik karakterét az
#     indexén keresztül. szo[0] a szó első karakterét adja vissza. Például, ha a szó "almafa", akkor szo[0] az "a"
#     karakter lesz.
#     2. szolanc[-1][-1]:
#     szolanc[-1]: A szolanc lista utolsó elemét adja vissza. A -1 index mindig az utolsó elemet jelöli a listában.
#     szolanc[-1][-1]: Az utolsó elem utolsó karakterét adja vissza. Az első [-1] kiválasztja a lista utolsó elemét
#     (tehát az utolsó szót), a második [-1] pedig ebből a szóból az utolsó karaktert adja vissza.
#     Például, ha a lista utolsó szava "lankad", akkor szolanc[-1] a "lankad" szó lesz,
#     és szolanc[-1][-1] az utolsó karakter, vagyis "d" lesz.
#     3. if szo[0] != szolanc[-1][-1]:
#     Ez a feltétel azt vizsgálja, hogy az aktuális szó első betűje nem egyezik-e meg az előző szó utolsó betűjével.
#     != azt jelenti, hogy "nem egyenlő". Tehát ha a két karakter nem egyezik meg, akkor a feltétel igaz lesz,
#     és a program végrehajtja a hozzá tartozó blokkot (megszakítja a ciklust, és kiírja, hogy "Nem illeszkedett!").

# Példa:
#
# Tegyük fel, hogy az előző szó a listában "lankad", és a felhasználó most a "durrog" szót adja meg:
#
#     - szo[0]: Az "durrog" első betűje "d".
#     - szolanc[-1][-1]: A "lankad" utolsó betűje is "d".
#     - Mivel ezek egyenlőek, a feltétel nem teljesül (hamis), és a játék folytatódik.
#
# Viszont, ha a felhasználó például a "gondos" szót adná meg:
#
#     - szo[0]: A "gondos" első betűje "g".
#     - szolanc[-1][-1]: A "lankad" utolsó betűje "d".
#     - Mivel "g" nem egyenlő "d"-vel, a feltétel igaz lesz, és a program kiírja, hogy "Nem illeszkedett!",
#     majd megszakítja a ciklust.

