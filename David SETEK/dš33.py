#doplnění kódu dš19.py
#vstupní data

height = input("Zadejte svou výšku v metrech:\n")
weight = input("Zadejte svou váhu v kilogramech:\n")

#BMI výpočet

BMI = int(weight)/(float(height) * float(height))
BMI = round(BMI,1)

if BMI < 18.5:
    print(f"Vaše BMI má hodnotu {BMI}. Patříte do kategorie - Podváha.")
elif BMI < 24.9:
    print(f"Vaše BMI má hodnotu {BMI}. Patříte do kategorie - Normální váha.")
elif BMI < 29.9:
    print(f"Vaše BMI má hodnotu {BMI}. Patříte do kategorie - Nadváha.")
elif BMI < 34.9:
    print(f"Vaše BMI má hodnotu {BMI}. Patříte do kategorie - Obezita.")
else:
    print(f"Vaše BMI má hodnotu {BMI}. Patříte do kategorie - Těžká obezita.")
