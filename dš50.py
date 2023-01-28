# Nejvyšší skóre

#score = [98, 50, 25, 78, 92]

#print(max(score))
#print(min(score))

score = input("Zadejte skóre jednotlivých studentů oddělené čárkou a mezerou:\n")
score_list = score.split(", ")
score_list_number = []
maximum = 0
minimum = 100

for index in range(0, len(score_list)):
    score_list_number.append(int(score_list[index]))

print(score_list_number) #původní list se stringy se převedl na čísla

for one_number in score_list_number:
    if one_number > maximum:
        maximum = one_number
    if one_number < minimum:
        minimum = one_number


print(f"Maximum je {maximum}.")
print(f"Minimum je {minimum}.")


