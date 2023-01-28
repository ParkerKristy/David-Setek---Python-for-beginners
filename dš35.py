# Návštěvník si nejdříve zvolí velikost pizzy (S, M, L). 
# Za velikost S se platí 100 Kč, za M 150 Kč a za L 200 Kč.

# Poté se zeptáte, zda chce feferonky. 
# Pokud ano, tak u velikosti S se bude platit 20 Kč navíc a u velikostí M a L 30 Kč navíc.

# Poté se ještě zeptáte, zda chce návštěvník sýr navíc. 
# Pokud ano, tak si připlatí dalších 15 Kč.

print("Vítejte v aplikaci na objednání pizzy!")
size = input("Jakou velikost pizzy chcete? S, M, L: ")
feferonky = input("Chcete navíc feferonky? A/N :")
cheese = input("Chcete navíc sýr  ? A/N :")

bill = 0

#Davidova verze
if size == "S":
    bill += 100 # bill = bill + 100
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

#moje verze


if size == "S":
    bill += 100
    if feferonky == "A":
        bill += 20

if size == "M":
    bill += 150
    if feferonky == "A":
        bill += 30


if size == "L":
    bill += 200
    if feferonky == "A":
        bill += 30

if cheese == "A":
    bill += 15
    
print(f"Celková cena: {bill}")
   
