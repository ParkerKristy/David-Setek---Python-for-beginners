set1 = ["⬛️", "⬛️", "⬛️"]
set2 = ["⬛️", "⬛️", "⬛️"]
set3 = ["⬛️", "⬛️", "⬛️"]

all_sets = [set1, set2, set3]
print(f"{set1}\n{set2}\n{set3}\n")

position = input("Zadejte souřadnice: (00 - 22) " )

num1 = int(position[0])
num2 = int(position[1])

all_sets[num1] [num2] = "X"

print(f"{set1}\n{set2}\n{set3}")