'''
stone = 1
paper = -1
scissor = 0
'''

import random 
computer = random.choice([-1,1,0])
print("Choose: stone=1, paper=-1, scissor=0")
youstr = input("Chose from the options")
dict = {"stone": 1,"paper": -1, "scissor": 0}
you = dict[youstr]
revDict = {1:"stone",-1:"paper",0:"scissor"}

print(f"you choose {revDict[you]}\ncomputer  choose {revDict[computer]}")

if computer == you:
    print("its a draw")
else:
    if computer == 1 and you == -1:
        print("you Win!")
    elif computer == 1 and you == 0:
        print("you lose!")
    elif computer == -1 and you == 0:
        print("you Win!")
    elif computer == -1 and you == 1:
        print("you lose!")
    elif computer == 0 and you == 1:
        print("you Win!")
    elif computer == 0 and you == -1:
        print("you lose!")