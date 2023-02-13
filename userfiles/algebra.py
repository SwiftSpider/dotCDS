import math
varname = list([])
vardata = list([])
varknown = list([])

dec = list("1234567890-")

def simplify(expression):
    knownval = 0
    for i in range(expression.split(" ")):
        isVar = False
        for x in range(len(expression.split(" ")[i])):
            if(expression.split(" ")[i][x] not in dec):
                isVar = True
        if(isVar == True):
            if(expression.split(" ")[i].split("/")[1] in varname):
                if(varknown[varname.index(expression.split(" ")[i].split("/")[1])]):
                    knownval += float(expression.split(" ")[i].split("/")[0])

problem = input("ALGEBRA:>> ")
