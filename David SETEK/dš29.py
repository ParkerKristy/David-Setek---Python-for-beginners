# Podmínky - vylepšení dš26.py

print("Vítejte na horské dráze")
height = int(input("Jaká je Vaše výška v cm?\n"))

if height >= 87:
    print("Můžete jet na horské dráze.")
    age = int(input("Jaký je Váš věk?\n"))
    if age < 18:
        print("Cena Vašeho lístku je 100 Kč")
    else:
        print("Cena Vašeho lístku je 150 Kč.")
else:
    print("Omlouváme se, ale na horské dráze jet nemůžete.")

