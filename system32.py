import os.path
import os

vardata = list([])
varname = list([])
pastCmd = list([])
vargloble = list([])

# if
# var
# = > < >= <=
# var
# command

# ifeq ifgt iflt ifge ifle
# var
# var
# command

alphabet = ("abcdefghifklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def getGlobeVar():
    file1 = open("globalvar", 'r')
    data = list([])
    for line in file1:
        if(line.strip() != ""):
            data.append(line.strip())
    
    for line in file1:
        compilecds(line.strip())
    file1.close()
    varname.append("REPLY")
    vardata.append(" ")

varinFile = 0
def varinfile(var,dfile):
    with open(dfile, 'r') as fp:
        for l_no, line in enumerate(fp):
            if var in line:
                varinFile = (l_no)
                return True
                break
            else:
                varinFile = (0)
                print("debug: var is not in file")
                return False

def compilecds(command):
    def mathreform():
        runPar[1] = cmdPar[0]
        runPar[3] = cmdPar[4]
    cmdPar = list(command.split(" "))
    runPar = list(command.split(" "))
    if(len(runPar) < 4):
        for i in range(4 - len(runPar)):
            runPar.append(0)

    if(runPar[1] == "="):
        if(len(cmdPar) == 5):
            if(cmdPar[3] == "+"):
                runPar[0] = "add"
                mathreform()
            elif(cmdPar[3] == "-"):
                runPar[0] = "minus"
                mathreform()
            elif(cmdPar[3] == "*"):
                runPar[0] = "multiply"
                mathreform()
            elif(cmdPar[3] == "/"):
                runPar[0] = "divide"
                mathreform()
            elif(cmdPar[3] == "^"):
                runPar[0] = "exponent"
                mathreform()
            elif(cmdPar[3] == "++"):
                runPar[0] = "join"
                mathreform()
            else:
                cdsError("operator unrecognized " + cmdPar[3])
        elif(len(cmdPar) == 3):
            runPar[0] = "set"
            runPar[1] = cmdPar[0]

        else:
            cdsError("var > or < needed")
    elif(cmdPar[0] == "write"):
        if(len(cmdPar) == 3):
            runPar[2] = cmdPar[2]
            for i in range(len(cmdPar) - 3):
                runPar[2] += " " + cmdPar[i + 3]
    elif(cmdPar[0] == "input"):
        if(len(cmdPar) == 2):
            runPar[1] = cmdPar[1]
            for i in range(len(cmdPar) - 2):
                runPar[1] += " " + cmdPar[i + 2]
    elif(cmdPar[0] == "if"):
        if(cmdPar[2] == "=="):
            runPar[0] = "ifeq"
            runPar[2] = cmdPar[3]
        elif(cmdPar[2] == ">"):
            runPar[0] = "ifgt"
            runPar[2] = cmdPar[3]
        elif(cmdPar[2] == "<"):
            runPar[0] = "iflt"
            runPar[2] = cmdPar[3]
        elif(cmdPar[2] in (">=","=>")):
            runPar[0] = "ifge"
            runPar[2] = cmdPar[3]
        elif(cmdPar[2] in ("<=","=<")):
            runPar[0] = "ifle"
            runPar[2] = cmdPar[3]
        elif(cmdPar[2] in ("!=","=!")):
            runPar[0] = "ifne"
            runPar[2] = cmdPar[3]
        if(len(cmdPar) == 4):
            runPar[3] = cmdPar[4]
        else:
            runPar[3] = cmdPar[4]
            for i in range(len(cmdPar) - 5):
                runPar[3] += " " + cmdPar[i + 5]
    elif(cmdPar[0] == "repeat"):
        if(len(cmdPar) == 3):
            runPar[2] = cmdPar[2]
            for i in range(len(cmdPar) - 3):
                runPar[2] += " " + cmdPar[i + 3]
    runCmd(runPar[0], runPar[1], runPar[2], runPar[3])

def FOrI(thing,isStringOK):
    if(thing in alphabet):
        if(isStringOK):
            return str(thing)
        else:
            cdsError("inputed string instead of number")
    elif("." in thing):
        return float(thing)
    else:
        return int(thing)

def runCmd(x,y,z,t):
    if(x == "help"):

        print("""help -gives you info of commands
read (file) -reads the given files contents
say (var) -writes out given variable
write (file) (thing) -writes in a script
new (type) (name) -creates new file or folder
(var) = (value) -sets var slot to given value
(var) = (var) (operation) (var) -math
clear (type) (name) -clears the file/folder (if clearing screen then dont use (name)
delete (type) (name) -deletes file/folder
child (folder) -says the children of that folder
run (file) -run a script in a specified language
varlist -lists all var names and data
if (var) (statement) (var) (command) -if whatever then do command
// (comment) -system skips this command
repeat (var) (command) -repeats command var times

scripts can contain commands in this format:
thing = hello_;other = world;done = thing ++ other;say done

two +'s joins the variables together ex.
helloworld = hello ++ world

:z -up arrow/goes to your last said command
:zz -second last
:zzz -so on

can only use var 0,1,2,3,4""")
        
    elif(x == "read"):

        if(os.path.exists("userfiles/" + y)):
            file = open("userfiles/" + y)
            print(file.read())
        else:
            cdsError("file doesnt exist")
        
    elif(x == "write"):
        if(os.path.exists("userfiles/" + y)):
            file = open("userfiles/" + y,"a")
            file.write("\n" + z)
            file.close()
        else:
            cdsError("file doesnt exist")
        
    elif(x == "set"):
        if("$" in y):
            if(z != "NULL"):
                if(varinfile(y.split("$")[1],"globalvar")):

                    #gethering file contents
                    with open('globalvar','r',encoding='utf-8') as file:
                        data = list(file.readlines())
                    newData = list([])

                    #gather names of variables
                    for i in range(len(data)):
                        newData.append(data[i].split(" ")[0])
                    
                    #isolating and resetting specific variable
                    data[newData.index(y.split("$")[1])] = newData[newData.index(y.split("$")[1])] + " = " + z

                    #wipe file
                    with open("globalvar",'r+') as file:
                        file.truncate(0)
                    
                    #putting list in file
                    file = open("globalvar","a")
                    for i in range(len(data)):
                        file.write(data[i])
                    file.close()

                    #setting local variable
                    vardata[varname.index(y.split("$")[1])] = z
                else:

                    file = open("globalvar","a")
                    file.write("\n" + y.split("$")[1] + " = " + z )
                    file.close()
                    varname.append(y.split("$")[1])
                    vardata.append(z)
            else:
                
                    #gethering file contents
                    with open('globalvar','r',encoding='utf-8') as file:
                        data = list(file.readlines())
                    newData = list([])

                    #gather names of variables
                    for i in range(len(data)):
                        newData.append(data[i].split(" ")[0])
                    
                    #isolating and blanking variable space out
                    data[newData.index(y.split("$")[1])] = ""

                    #wipe file
                    with open("globalvar",'r+') as file:
                        file.truncate(0)
                    
                    #putting list in file
                    file = open("globalvar","a")
                    for i in range(len(data)):
                        file.write(data[i])
                    file.close()

                    #setting local variable
                    vardata[varname.index(y.split("$")[1])] = ""
        else:
            if(y in varname):
                vardata[varname.index(y)] = z
            else:
                varname.append(y)
                vardata.append(z)
        
    elif(x == "say"):
        
        if(y in varname):
            print(vardata[varname.index(y)])
        else:
            cdsError("var doesnt exist")
        
    elif(x == "new"):
        
        if(y == "file"):
            if(os.path.exists("userfiles/" + z) == False):
                file = open("userfiles/" + z,"a")
                file.write("")
                file.close()
                
        elif(y == "folder"):
            if(os.path.exists("userfiles/" + z) == False):
                os.mkdir("userfiles/" + z)
        else:
            cdsError("unkown file type: " + y)
        
    elif(x == "add"):
        
        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = str(FOrI(vardata[varname.index(z)],False) + FOrI(vardata[varname.index(t)],False))
                else:
                    varname.append(y)
                    vardata.append(str(FOrI(vardata[varname.index(z)],False) + FOrI(vardata[varname.index(t)],False)))
            else:
                cdsError("var doesnt exist")
        else:
            cdsError("var doesnt exist")
        
    elif(x == "minus"):
        
        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = str(FOrI(vardata[varname.index(z)],False) - FOrI(vardata[varname.index(t)],False))
                else:
                    varname.append(y)
                    vardata.append(str(FOrI(vardata[varname.index(z)],False) - FOrI(vardata[varname.index(t)],False)))
            else:
                cdsError("var doesnt exist")
        else:
            cdsError("var doesnt exist")
        
    elif(x == "multiply"):
        
        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = str(FOrI(vardata[varname.index(z)],False) * FOrI(vardata[varname.index(t)],False))
                else:
                    varname.append(y)
                    vardata.append(str(FOrI(vardata[varname.index(z)],False) * FOrI(vardata[varname.index(t)],False)))
            else:
                cdsError("var doesnt exist")
        else:
            cdsError("var doesnt exist")
        
    elif(x == "divide"):

        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = str(FOrI(vardata[varname.index(z)],False) / FOrI(vardata[varname.index(t)],False))
                else:
                    varname.append(y)
                    vardata.append(str(FOrI(vardata[varname.index(z)],False) / FOrI(vardata[varname.index(t)],False)))
            else:
                cdsError("var doesnt exist")
        else:
            cdsError("var doesnt exist")
    
    elif(x == "exponent"):

        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = str(FOrI(vardata[varname.index(z)],False) ** FOrI(vardata[varname.index(t)],False))
                else:
                    varname.append(y)
                    vardata.append(str(FOrI(vardata[varname.index(z)],False) ** FOrI(vardata[varname.index(t)],False)))
            else:
                cdsError("var doesnt exist")
        else:
            cdsError("var doesnt exist")

    elif(x == "join"):

        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = vardata[varname.index(z)] + vardata[varname.index(t)]
                else:
                    varname.append(y)
                    vardata.append(vardata[varname.index(z)] + vardata[varname.index(t)])
            else:
                cdsError("var doesnt exist")
        else:
            cdsError("var doesnt exist")
            
    elif(x == "clear"):

        if(y == "screen"):
            os.system("clear")
        elif(y == "file"):
            if(os.path.exists("userfiles/" + z)):
                with open("userfiles/" + z,'r+') as file:
                    file.truncate(0)
        elif(y == "folder"):
            listdir = os.listdir("userfiles/" + z)
            for i in range(len(os.listdir("userfiles/" + z))):
                os.remove("userfiles/" + z + "/" + listdir[i])
        
    elif(x == "delete"):
        
        if(os.path.exists("userfiles/" + z)):
            if(y == "file"):
                os.remove("userfiles/" + z)
            elif(y == "folder"):
                if(len(os.listdir("userfiles/" + z)) == 0):
                    os.rmdir("userfiles/" + z)
                else:
                    listdir = os.listdir("userfiles/" + z)
                    for i in range(len(os.listdir("userfiles/" + z))):
                        os.remove("userfiles/" + z + "/" + listdir[i])
                    os.rmdir("userfiles/" + z)
        else:
            cdsError("file doesnt exist")

    elif(x == "child"):

        if(y == "0"):
            print(os.listdir("userfiles"))
        else:
            if(os.path.exists("userfiles/" + str(y))):
                print(os.listdir("userfiles/" + y))
            else:
                cdsError("folder doesnt exist")

    elif(x == "run"):

        if(os.path.exists("userfiles/" + y)):
            ftype = y
            fRom = ftype.split(".")
            ftype = fRom[len(fRom)-1]

            if(ftype == "cds"):
                file1 = open("userfiles/" + y, 'r')
                for line in file1:
                    linestrip = line.strip()
                    for i in range(len(linestrip.split(";"))):
                        if(linestrip.split(";")[i] != ""):
                            compilecds(linestrip.split(";")[i])
                file1.close()

            elif(ftype == "py"):
                os.system("python3 userfiles/" + y)
            elif(ftype == "js"):
                os.system("node userfiles/" + y)
            else:
                cdsError("sorry language not supported")
        else:
            cdsError("file doesnt exist")

    elif(x == "varlist"):
        
        for i in range(len(varname)):
            print(varname[i] + " : " + vardata[i])

    elif(x == "//"):
        pass
    
    elif(x == "ifeq"):
        if(FOrI(vardata[varname.index(y)],False) == FOrI(vardata[varname.index(y)],False)):
            for i in range(len(t.split(";"))):
                if(t.split(";")[i] != ""):
                    compilecds(t.split(";")[i])
    elif(x == "ifgt"):
        if(FOrI(vardata[varname.index(y)],False) > FOrI(vardata[varname.index(y)],False)):
            for i in range(len(t.split(";"))):
                if(t.split(";")[i] != ""):
                    compilecds(t.split(";")[i])
    elif(x == "iflt"):
        if(FOrI(vardata[varname.index(y)],False) < FOrI(vardata[varname.index(y)],False)):
            for i in range(len(t.split(";"))):
                if(t.split(";")[i] != ""):
                    compilecds(t.split(";")[i])
    elif(x == "ifge"):
        if(FOrI(vardata[varname.index(y)],False) >= FOrI(vardata[varname.index(y)],False)):
            for i in range(len(t.split(";"))):
                if(t.split(";")[i] != ""):
                    compilecds(t.split(";")[i])
    elif(x == "ifle"):
        if(FOrI(vardata[varname.index(y)],False) <= FOrI(vardata[varname.index(y)],False)):
            for i in range(len(t.split(";"))):
                if(t.split(";")[i] != ""):
                    compilecds(t.split(";")[i])
    elif(x == "ifne"):
        if(FOrI(vardata[varname.index(y)],False) != FOrI(vardata[varname.index(y)],False)):
            for i in range(len(t.split(";"))):
                if(t.split(";")[i] != ""):
                    compilecds(t.split(";")[i])
    
    elif(x == "input"):
        vardata[varname.index("REPLY")] = input(y)
        for i in range(len(t.split(";"))):
            if(t.split(";")[i] != ""):
                compilecds(t.split(";")[i])
    
    elif(x == "repeat"):
        for i in range(FOrI(vardata[varname.index(y)],False)): #error "5 not in list" var funf = 5
            for i in range(len(z.split(";"))):
                if(z.split(";")[i] != ""):
                    compilecds(z.split(";")[i])

    else:
        cdsError("command unrecognized " + x)

def cdsError(msg):
    print("\n\033[1;31m! " + msg + " !\033[1;0m\n")

getGlobeVar()
print("""dotCDS 1.3 (system32, Jan 28 2023, 9:12) 
[Powered and run by Python3] on linux
Type "help" if you are unsure what to do.
""")
while(True):
    cmdRom = input(">> ")
    if(cmdRom != ""):
        cZplacement = 1
        if(cmdRom[0] == ":"):
            amountZ = cmdRom.count("z")
            for i in range(amountZ):
                cZplacement += i
            compilecds(pastCmd[len(pastCmd) - cZplacement])
        else:
            pastCmd.append(cmdRom)
            for i in range(len(cmdRom.split(";"))):
                if(cmdRom.split(";")[i] != ""):
                    compilecds(cmdRom.split(";")[i])