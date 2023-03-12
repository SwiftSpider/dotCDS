import time
import math
import random
areas = list(("alaska","northwest territory","alberta","ontario","eastern canada","greenland","western united states","eastern united states","central america","venezuela","brazil","peru","argentina","north africa","egypt","east africa","central africa","south africa","madagascar","western europe","southern europe","great britain","iceland","scandinavia","northern europe","russia","ural","siberia","yakutsk","kamchatka","irkutsk","afghanistan","mongolia","japan","china","middle east","india","southeast asia","indonesia","new guinea","western australia","eastern australia"))
northAmerica = list((0,1,2,3,4,5,6,7,8))
southAmerica = list((9,10,11,12))
africa = list((13,14,15,16,17,18))
europe = list((19,20,21,22,23,24,25))
asia = list((26,27,28,29,30,31,32,33,34,35,36,37))
australia = list((38,39,40,41))
actions = list(("riots","wild fires","depression","inflation","police brutallity","racism"))
good = list(("deflation","happiness","trust","unifacation"))
nationind = list((9,4,6,7,12,4))
nations = list(("north america","south america","africa","europe","asia","australia"))
point = list((5,2,3,5,7,2))
def dmi(x):
    point[x] -= random.randint(0,round(point[x]/2))
def dpl(x):
    point[x] += random.randint(0,round(point[x]/2))
print(len(areas))
while True:
    print()
    time.sleep(random.randint(4,5))
    state = random.randint(0,len(areas)-1)
    if(random.randint(0,1) == 0):
        print(areas[state] + " is suffering from " + actions[random.randint(0,len(actions)-1)])
        if(state in northAmerica):
            dmi(0)
        elif(state in southAmerica):
            dmi(1)
        elif(state in africa):
            dmi(2)
        elif(state in europe):
            dmi(3)
        elif(state in asia):
            dmi(4)
        elif(state in australia):
            dmi(5)
    else:
        print(areas[state] + " is eased by " + good[random.randint(0,len(good)-1)])
        if(state in northAmerica):
            dpl(0)
        elif(state in southAmerica):
            dpl(1)
        elif(state in africa):
            dpl(2)
        elif(state in europe):
            dpl(3)
        elif(state in asia):
            dpl(4)
        elif(state in australia):
            dpl(5)
    time.sleep(random.randint(4,5))
    print()
    for i in range(6):
        print(nations[i] + " ~ " + str(point[i]))