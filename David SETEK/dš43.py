#List

employees = ["David", "Harry", "Ron"]
print(employees)
print(employees [0])
print(employees [1])
print(employees [2])

print(employees [-1])
print(employees [-2])
print(employees [-3])

#Změna položky 
employees[1] = "Hermiona"
print(employees)

# Přidání obsahu .append na konec listu
employees.append("Harry")
print(employees)

# Přídání více položek .extend
employees.extend(["Hagrid", "Draco"])
print(employees)

# Odtranění položky .remove
employees.remove("Ron")
print(employees)