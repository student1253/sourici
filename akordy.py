import random
space = 30 * "-"

print('''Zde tě budu testovat na akordy, zadám ti stupnici a jaký akord máš vytvořit.
    Tvůj výstup pro zadání C kvintakord bude: c, e, g
    Pro ukončení programu napoiš "stop"''')
vstupy = input("Pro pokračování stiskni entr ")
print(space)

stupnice = ["C", "G", "D", "A", "E", "H", "Fis", "Csi", "F", "B", "Es", "As", "Des", "Ges", "Ces"]
akordy = [["c", "e", "g"], 
          ["g", "h", "d"],
          ["d", "fis", "a"],
          ["a", "cis", "e"],
          ["e", "gis", "h"], 
          ["h", "dis", "fis"], 
          ["fis", "ais", "cis"], 
          ["cis", "eis", "gis"], 
          ["f", "a", "c"], 
          ["b", "d", "f"], 
          ["es", "g", "b"], 
          ["as", "c", "es"], 
          ["des", "f", "as"], 
          ["ges", "b", "des"], 
          ["ces", "es", "ges"]]
typy = ["kvintakord", "sextakord", "kvartsextakord"]

def vyhodnoceni(vstup, typ, predznamenani):
    odpoved = [x.strip().lower() for x in vstup.split(",")]
    if typ == "kvintakord":
        return odpoved == akordy[predznamenani]
    elif typ == "sextakord":
        return odpoved == akordy[predznamenani][1:] + akordy[predznamenani][:1]
    else:
        return odpoved == akordy[predznamenani][2:] + akordy[predznamenani][:2]

while vstupy != "stop":
    predznamenani = random.randint(0, 14)
    typakordu = random.choice(typy)
    otazka = stupnice[predznamenani]
    while not vyhodnoceni(vstupy, typakordu, predznamenani) and vstupy != "stop":
        vstupy = input(f"{typakordu} {otazka} dur: ")
    print(f"Správně\n{space}")