print("Vítejte v aplikaci na objednání pizzy!")
size = input("Jakou velikost pizzy chcete? S, M, L: ")
feferonky = input("Chcete navíc feferonky? A/N :")
cheese = input("Chcete navíc sýr  ? A/N :")
bill = 0
#Davidova verze
if size == "S":
    bill += 100
elif size == "M":
    bill += 150
elif size == "L":
    bill += 200 

if feferonky == "A":
    if size == "S":
        bill += 20
    else:
        bill += 30

if cheese == "A":
    bill += 15

print(f"Celková částka: {bill} Kč.")