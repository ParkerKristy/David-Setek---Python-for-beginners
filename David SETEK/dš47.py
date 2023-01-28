import random

 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
 
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
 
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
all_list=[rock, paper, scissors]

user_choice = int(input("Co si vybere? 0 = kámen, 1 = papír, 2 = nůžky\n"))
print(f"Uživatel si vybral:\n{all_list[user_choice]}")

computer_choice = random.randint(0,2)
print(f"Počítač si vybral:\n{all_list[computer_choice]}")

if user_choice == computer_choice:
    print ("Remíza. Hraj znovu")
elif user_choice == 0 and computer_choice == 1:
    print("Papír balí kámen. Prohrál jsi.") 
elif user_choice == 0 and computer_choice == 2:
    print("Kámen tupí nůžky. Vyhrál jsi!") 
elif user_choice == 1 and computer_choice == 0:
    print("Papír balí kámen. Vyhrál jsi!") 
elif user_choice == 1 and computer_choice == 2:
    print("Nůžky stříhají papír. Prohrál jsi.") 
elif user_choice == 2 and computer_choice == 0:
    print("Kámen tupí nůžky. Prohrál jsi.") 
elif user_choice == 2 and computer_choice == 1:
    print("Nůžky stříhají papír. Vyhrál jsi!")

