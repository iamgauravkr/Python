import random

target = random.randint(1, 100)
while True:
    userchoice = (input("Guess the Target or Quit(Q): "))
    if(userchoice == "Q"):
        break

    userchoice = int(userchoice)
    if(userchoice == target):
        print("Success: Correct guess ")
        break 
    elif(userchoice < target):
        print("your choice is smaller than target. Take a bigger Guess... ")
    else:
        print("your choice is bigger than target. Take a smaller Guess... ")


print("------Game Over-----")
