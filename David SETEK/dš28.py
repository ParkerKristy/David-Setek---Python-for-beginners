# Podmínky - normal, smart, extrasmart

type = input("Jaký chcete typ mobilního telefonu? Možnosti: normal, smart, extrasmart\n")

#if type == "normal":
#    print(f"Cena telefonu typu {type} je 15 000 Kč.")
#else:
 #   print(f"Cena telefonu typu {type} je 25 000 Kč.")


if type != "normal":
    print(f"Cena telefonu typu {type} je 25 000 Kč.")
else:
    print(f"Cena telefonu typu {type} je 15 000 Kč.")

#rozdílné ceny pro každý typ telefonu
type = input("Jaký chcete typ mobilního telefonu? Možnosti: normal, smart, extrasmart\n")
if type == "normal":
    print(f"Cena telefonu typu {type} je 15 000 Kč.")
if type == "smart":
    print(f"Cena telefonu typu {type} je 20 000 Kč.")
else:
    print(f"Cena telefonu typu {type} je 25 000 Kč.")

# Znaménka
# ==
# <, >
# <=, >=
# != nerovná se