getal = int(input("Geef een getal tussen 1 en 10: "))

# Optioneel: invoer controleren
while getal < 1 or getal > 10:
    print("Ongeldige invoer. Probeer opnieuw.")
    getal = int(input("Geef een getal tussen 1 en 10: "))

print(f"\nTafel van {getal}:")

for i in range(1, 11):
    resultaat = getal * i
    print(f"{getal} x {i} = {resultaat}")