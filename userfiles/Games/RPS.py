import time
import random
print("say stop if you want to stop")
choices = list(("Rock","Paper","Scissors"))
pchoices = list(("r","p","s"))
choice = ""
aiwins = 0
plwins = 0
while choice != "stop":
    time.sleep(0.8)
    print("rock...")
    time.sleep(0.8)
    print("paper...")
    time.sleep(0.8)
    print("scissors...")
    choice = input("< make your choice r/p/s > ")
    if(choice != "stop" and choice in pchoices):
        print("SHOOT!")
        time.sleep(1.1)
        aichoice = random.randint(0,2)
        print(choices[aichoice] + " vs " + choices[pchoices.index(choice)])
        time.sleep(1.1)
        choice = pchoices.index(choice)
        print()
        if(aichoice == choice):
            print("DRAW")
        elif(aichoice == 0 and choice == 2):
            print("YOU LOSE")
            aiwins += 1
        elif(aichoice == 2 and choice == 0):
            print("YOU WIN")
            plwins += 1
        elif(aichoice > choice):
            print("YOU LOSE")
            aiwins += 1
        elif(aichoice < choice):
            print("YOU WIN")
            plwins += 1
        else:
            print("ERROR")
            choice = "stop"
        print()
        print(str(plwins) + " : " + str(aiwins))