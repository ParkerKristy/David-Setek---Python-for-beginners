print("Vítejte v kalkulátoru na výpočet plateb")
payment = int(input("Kolik máte celkem zaplatit? "))

tip = int(input("Kolik chcete dát spropitného (v %) "))

division = int(input("Mezi kolik lidí se má rozdělit částka? "))


total = (payment + (payment * tip / 100)) / division
final_payment = "{:.2f}".format(total)

print(f"Každý člověk má zapltit {final_payment} Kč")


# print("{:.2f}".format(3.1415926));