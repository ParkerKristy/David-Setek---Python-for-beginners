print("Vítejte v kalkulátoru na výpočet plateb")
payment = int(input("Kolik máte celkem zaplatit? "))

tip = int(input("Kolik chcete dát spropitného (v %) "))

division = int(input("Mezi kolik lidí se má rozdělit částka? "))


total = (payment + (payment * tip / 100)) / division

print(f"Každý člověk má zapltit {total} Kč")

