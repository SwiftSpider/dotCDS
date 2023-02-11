import os
import time

def update():
    os.system("clear")
    print("to choose were to go it is 1-9")
    print("upper,right is 3")
    print("lower,left is 7")
    print()
    for i in range(len(log)):
        print(log[i])
    print()
    print(end[chart[0]] + "|" + end[chart[1]] + "|" + end[chart[2]])
    print(mid[chart[0]] + "|" + mid[chart[1]] + "|" + mid[chart[2]])
    print(mid[chart[0]] + "|" + mid[chart[1]] + "|" + mid[chart[2]])
    print(end[chart[0]] + "|" + end[chart[1]] + "|" + end[chart[2]])
    print(breaker)
    print(end[chart[3]] + "|" + end[chart[4]] + "|" + end[chart[5]])
    print(mid[chart[3]] + "|" + mid[chart[4]] + "|" + mid[chart[5]])
    print(mid[chart[3]] + "|" + mid[chart[4]] + "|" + mid[chart[5]])
    print(end[chart[3]] + "|" + end[chart[4]] + "|" + end[chart[5]])
    print(breaker)
    print(end[chart[6]] + "|" + end[chart[7]] + "|" + end[chart[8]])
    print(mid[chart[6]] + "|" + mid[chart[7]] + "|" + mid[chart[8]])
    print(mid[chart[6]] + "|" + mid[chart[7]] + "|" + mid[chart[8]])
    print(end[chart[6]] + "|" + end[chart[7]] + "|" + end[chart[8]])
    print()

def turn(player,letter):
    choice = int(input("Player: " + letter + "- make a move >>")) - 1
    log.append("Player " + letter + "- make a move >>" + str(choice + 1))
    if(chart[choice] != 0):
        print("\033[1;31malready filled\033[1;0m")
    else:
        chart[choice] = player
    update()

    #win check
    for i in range(len(winning)):
        print(winning)
        print(choice)
        print(type(choice))
        for x in range(3):
            if(str(choice+1) in str(winning[i])[x]):
                checkprog = 0
                for x in range(3):
                    rom = str(winning[i])
                    if(rom[x] == str(player)):
                        checkprog += 1
                print(checkprog)
                if(checkprog == 3):
                    print("PLAYER " + letter + " WINS")
                    time.sleep(3)
                    break

end = ("      "," #### "," #  # ")
mid = ("      "," #  # ","  ##  ")
breaker = ("------|------|------")

chart = list((0,0,0,0,0,0,0,0,0))

winning = list((678,630,642,852,840,210))

log = list([])

os.system("clear")
print("to choose were to go it is 1-9")
print("upper,right is 3")
print("lower,left is 7")
print()
print(end[0] + "|" + end[0] + "|" + end[0])
print(mid[0] + "|" + mid[0] + "|" + mid[0])
print(mid[0] + "|" + mid[0] + "|" + mid[0])
print(end[0] + "|" + end[0] + "|" + end[0])
print(breaker)
print(end[0] + "|" + end[0] + "|" + end[0])
print(mid[0] + "|" + mid[0] + "|" + mid[0])
print(mid[0] + "|" + mid[0] + "|" + mid[0])
print(end[0] + "|" + end[0] + "|" + end[0])
print(breaker)
print(end[0] + "|" + end[0] + "|" + end[0])
print(mid[0] + "|" + mid[0] + "|" + mid[0])
print(mid[0] + "|" + mid[0] + "|" + mid[0])
print(end[0] + "|" + end[0] + "|" + end[0])
print()
while True:
    turn(1,"O")
    turn(2,"X")