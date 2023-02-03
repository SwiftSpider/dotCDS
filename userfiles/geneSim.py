import random
import time
genePool = list()
romGen = list([])
AGene = "Aa"
genePool.append(AGene[random.randint(0,1)] + AGene[random.randint(0,1)])
genePool.append(AGene[random.randint(0,1)] + AGene[random.randint(0,1)])

# genePool = ("Aa","Aa")

square = list([])

def fillsqu(par1,par2):
    square = list([])
    square.append(par1[0] + par2[0])
    square.append(par1[1] + par2[0])
    square.append(par1[0] + par2[1])
    square.append(par1[1] + par2[1])

while True:
    romGen = list([])
    for i in range(int(len(genePool)/2)):
        romGen.append(genePool[i*2][random.randint(0,1)] + genePool[(i*2)+1][random.randint(0,1)])
        romGen.append(genePool[i*2][random.randint(0,1)] + genePool[(i*2)+1][random.randint(0,1)])
        romGen.append(genePool[i*2][random.randint(0,1)] + genePool[(i*2)+1][random.randint(0,1)])
        romGen.append(genePool[i*2][random.randint(0,1)] + genePool[(i*2)+1][random.randint(0,1)])
    print(genePool)
    time.sleep(1)
    print()
    print("--------------------")
    print()
    genePool = romGen