age = input('Zadejte svůj věk:\n')

remain = 90 - int(age)
months = remain * 12
weeks = remain * 52
days =  remain * 365


print(f"Zbývá vám {remain} let,\ncož je {months} měsíců,\ncož je {weeks} týdnů,\ncož je {days} dnů života.")