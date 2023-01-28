# Přestupný rok
# Kdy je rok přestupný?
# Rok musí být dělitelný 4
# Pokud není zároveň dělitelný 100
# tak je to přestupný rok
# Pokud je dělitelný 4, ale je dělitelný 100 a zároveň je dělitelný 400, 
# tak je to také přestupný rok


variable_year = int(input("Zadejte rok:\n"))

if (variable_year % 100 != 0) or (variable_year % 400 == 0 and variable_year % 4 == 0):
    print(f"Rok {variable_year} je rok přestupný.")
else:
    print(f"Rok {variable_year} je rok nepřestupný.")

        
#Davidova verze
year = int(input("Zadejte rok:\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Je to přestupný rok.")
        else:
            print("Není to přetupný rok.")
    else:
        print("Je to přestupný rok.")
else:
    print("Není to přestupný rok.")