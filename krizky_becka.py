import random
space = "-"*30

print("Ahojda, pojď si procvičovat stupnice s křížky a béčky.")
vstup = input("Pokud chceš hádat názvy podle předznamenání, napiš: název.\nPokud to chceš obráceně, napiš: předznamenání\n :  ")
print(space)

while vstup not in ["název", "předznamenání"]:
    vstup = input("Toto není jedna z možností, zkus to znovu: ")
    print(space)

stupnice = {"C" : "0", 
            "G" : "1#", 
            "D" : "2#", 
            "A" : "3#", 
            "E" : "4#", 
            "H" : "5#",
            "Fis" : "6#",
            "Cis" : "7#",
            "F" : "1b",
            "B" : "2b",
            "Es" : "3b",
            "As" : "4b",
            "Des" : "5b",
            "Ges" : "6b",
            "Ces" : "7b"}

if vstup == "název":
    while vstup != "stop":
        otazka = random.choice(list(stupnice.values()))
        while not(vstup in stupnice and stupnice[vstup] == otazka) and vstup != "stop":
            vstup = input(f"Jaký název má stupnice s předznamenáním {otazka}: ")
        print("Správně!")
        print(space)

else:
    while vstup != "stop":
        otazka = random.choice(list(stupnice.keys()))
        while vstup != stupnice[otazka] and vstup != "stop":
            vstup = input(f"Jaké předznamenání má stupnice s názvem {otazka}: ")
        print("Správně!")
        print(space)