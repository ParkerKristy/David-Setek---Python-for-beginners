#vstupní data

height = input("Zadejte svou výšku v metrech:\n")
weight = input("Zadejte svou váhu v kilogramech:\n")

#BMI výpočet

BMI = int(weight)/(float(height) * float(height))
print("Vaše BMI je:", round(BMI,2)) 