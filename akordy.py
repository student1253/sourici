import random
space = 30 * "-"

print('''Zde tě budu testovat na akordy, zadám ti stupnici a jaký akord máš vytvořit.
    Tvůj výstup pro zadání C kvintakord bude: c, e, g
    Pro ukončení programu napoiš "stop"''')
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

vstup = input("Chápeš to:")

while vstup != "stop":
    otazka = stupnice[random.randint(0, 14)]
    while vstup.split(",") != akordy[stupnice]:
        vstup = input(f"Kvintakord {otazka} dur: ")
    print(f"Správně\n{space}")