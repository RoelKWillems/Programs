naam_product = input("naam van het product?: ")
prijs_product = int(input("Wat is de prijs van het product?: "))
aantal_stuks = int(input("Hoeveel stuks wil je kopen?: "))

print(f"Je kocht {aantal_stuks} stuks van het product {naam_product}")
print(f"totaalbedrag: {aantal_stuks * prijs_product}")