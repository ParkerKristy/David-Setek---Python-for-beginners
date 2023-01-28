heights = input("Vložte výšky oddělené čárkou a mezerou\n")
heights_list = heights.split(", ")
suma = 0
for one_height in heights_list:
    suma = suma + int(one_height)

aveg = suma / len(heights_list)

print(f"Průměrná výška je: {aveg}")
