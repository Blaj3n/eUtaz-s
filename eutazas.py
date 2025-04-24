print("1. feladat")

eutazasok = []
eutazas = {}
with open("utasadat.txt", "r", encoding="utf-8") as file:
    for egysor in file:
        egysor = egysor.strip().split()
        eutazas["megallo"] = int(egysor[0])
        eutazas["datum"] = egysor[1].split("-")[0]
        eutazas["ido"] = egysor[1].split("-")[1]
        eutazas["kartya"] = egysor[2]
        eutazas["jegy_berlet"] = egysor[3]
        eutazas["ervenyesseg_db"] = egysor[4]
        eutazasok.append(eutazas)
        eutazas = {}
print(eutazasok)

print()

print("2. feladat")

szamlalo = 0
for utazas in eutazasok:
    szamlalo += 1
print(f"A buszra {szamlalo} utas akart felszállni.")
# print(f"A buszra {len(eutazasok)} utas akart felszállni.")

print("3. feladat")
szamlalo = 0
for utazas in eutazasok:
    if ((utazas["jegy_berlet"] == "JGY" and utazas["ervenyesseg_db"] == 0) or
            (utazas["jegy_berlet"] != "JGY" and utazas["datum"] > utazas["ervenyesseg_db"])):
        szamlalo += 1

print(f"A buszra {szamlalo} utas nem szállhatott fel.")

print("4. feladat")
busz_felszallok = []
for i in range(0, 30):
    szamlalo = 0
    for egyelem in eutazasok:
        if egyelem["megallo"] == i:
            szamlalo += 1
    busz_felszallok.append(szamlalo)
for i in range(0, 30):
    if busz_felszallok[i] == max(busz_felszallok):
        print(f"A legtöbb utas ({max(busz_felszallok)} fő) a {i}. megállóban próbált felszállni.")
        break

# kedvezménnyel (TAB, NYB)
# ingyenes (NYP, RVS, GYK)
print("5. feladat")
kedv_szamlalo = 0
ingy_szamlalo = 0
for utazas in eutazasok:
    if utazas["jegy_berlet"] != "JGY" and utazas["datum"] <= utazas["ervenyesseg_db"]:
        if utazas["jegy_berlet"] in ["TAB", "NYB"]:
            kedv_szamlalo += 1
        elif utazas["jegy_berlet"] in ["NYP", "RVS", "GYK"]:
            ingy_szamlalo += 1
print(f"Ingyenesen utazók száma: {ingy_szamlalo} fő")
print(f"A kedvezményesen utazók száma: {kedv_szamlalo} fő")



