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