import random
import time
import math
genePool = list([])
plants = 100
romGen = list([])
AGene = "Aa"
for i in range(6):
    genePool.append(AGene)

# genePool = ("Aa","Aa")
NumGen = 0
while True:
    NumGen += 1
    plants = math.floor(plants * 1.3)
    romGen = list([])
    done = list([])
    for i in range(int(len(genePool)/2)):
        select1 = random.randint(0,len(genePool)-1)
        while select1 in done:
            if(select1 not in done):
                break
            select1 = random.randint(0,len(genePool)-1)
        select2 = random.randint(0,len(genePool)-1)
        while select2 in done:
            if(select2 not in done):
                break
            select2 = random.randint(0,len(genePool)-1)
        rom = random.randint(1,math.ceil(plants / 50))
        if(plants >= rom):
            plants -= rom
            for x in range(rom):
                romGen.append(genePool[select1][random.randint(0,1)] + genePool[select2][random.randint(0,1)])
        
    #if(len(romGen) > random.randint(500,550)):
    #    romGen = list(romGen)
    #    genePool = list([])
    #    for i in range(random.randint(400,500)):
    #        genePool.append(romGen[i])
    #else:
    genePool = romGen


    heteroper = 0
    homorecper = 0
    homodomper = 0
    for i in range(len(genePool)):
        if(genePool[i] in ("Aa","aA")):
            heteroper += 1
            genePool[i] = "Aa"
        elif(genePool[i] == "AA"):
            homodomper += 1
        elif(genePool[i] == "aa"):
            homorecper += 1
    homodomper = round(homodomper / len(genePool) * 100)
    heteroper = round(heteroper / len(genePool) * 100)
    homorecper = round(homorecper / len(genePool) * 100)
    #homodomper /= len(romGen)
    #heteroper /= len(romGen)
    #homorecper /= len(romGen)
    for i in range(len(genePool)):
        print(genePool[i])
    print()
    print("Generation: " + str(NumGen))
    print(str(len(genePool)) + " organisms")
    print(str(plants) + " plants")
    print(str(homodomper) + "% AA")
    print(str(heteroper) + "% Aa")
    print(str(homorecper) + "% aa")
    time.sleep(1)
    print()
    print("--------------------")
    print()
    