import os.path
import os

vardata = list([])
varname = list([])
pastCmd = list([])

def compileCis(command):
    cmdPar = list(command.split(" "))
    runPar = list(command.split(" "))
    if(len(runPar) < 4):
        for i in range(4 - len(runPar)):
            runPar.append(0)

    if(runPar[1] == "="):
        if(len(cmdPar) == 5):
            if(cmdPar[3] == "+"):
                runPar[0] = "add"
                runPar[1] = cmdPar[0]
                runPar[2] = cmdPar[2]
                runPar[3] = cmdPar[4]
            elif(cmdPar[3] == "-"):
                runPar[0] = "minus"
                runPar[1] = cmdPar[0]
                runPar[2] = cmdPar[2]
                runPar[3] = cmdPar[4]
            elif(cmdPar[3] == "*"):
                runPar[0] = "multiply"
                runPar[1] = cmdPar[0]
                runPar[2] = cmdPar[2]
                runPar[3] = cmdPar[4]
            elif(cmdPar[3] == "/"):
                runPar[0] = "divide"
                runPar[1] = cmdPar[0]
                runPar[2] = cmdPar[2]
                runPar[3] = cmdPar[4]
            elif(cmdPar[3] == "^"):
                runPar[0] = "exponent"
                runPar[1] = cmdPar[0]
                runPar[2] = cmdPar[2]
                runPar[3] = cmdPar[4]
            elif(cmdPar[3] == "++"):
                runPar[0] = "join"
                runPar[1] = cmdPar[0]
                runPar[2] = cmdPar[2]
                runPar[3] = cmdPar[4]
            else:
                cisError("operator unrecognized " + cmdPar[3])
        elif(len(cmdPar) == 3):
            runPar[0] = "set"
            runPar[1] = cmdPar[0]
            runPar[2] = cmdPar[2]

        else:
            cisError("var > or < needed")
    elif(cmdPar[0] == "write"):
        if(len(cmdPar) == 3):
            runPar[2] = cmdPar[2]
        else:
            runPar[2] = cmdPar[2] + " "
            for i in range(len(cmdPar) - 3):
                runPar[2] = cmdPar[i + 3]
    runCmd(runPar[0], runPar[1], runPar[2], runPar[3])

def FOrI(thing):
    if("." in thing):
        return float(thing)
    else:
        return int(thing)

def runCmd(x,y,z,t):
    if(x == "help"):
        print("""help -gives you info of commands
read (file) -reads the given files contents
say (var slot) -writes out given variable
write (file) (thing) -writes in a script
new (type) (name) -creates new file or folder
(var) = (value) -sets var slot to given value
(var) = (var) (operation) (var) -math
clear (type) (name) -clears the file/folder (if clearing screen then dont use (name)
delete (type) (name) -deletes file/folder
child (folder) -says the children of that folder
run (file) -run a script in a specified language
vardata -shows all variable data
varname -shows all variable names

two +'s joins the variables together ex.
helloworld = hello ++ world

:z -up arrow/goes to your last said command
:zz -second last
:zzz -so on

can only use var 0,1,2,3,4""")
        
    elif(x == "read"):
        
        if(os.path.exists(y)):
            file = open("userfiles/" + y)
            print(file.read() + "\n")
        else:
            cisError("file doesnt exist")
        
    elif(x == "write"):
        
        if(os.path.exists(y)):
            file = open("userfiles/" + y,"a")
            file.write(z)
            file.close()
        else:
            cisError("file doesnt exist")
        
    elif(x == "set"):
        
        if(y in varname):
            vardata[varname.index(y)] = z
        else:
            varname.append(y)
            vardata.append(z)
        
    elif(x == "say"):
        
        if(y in varname):
            print(vardata[varname.index(y)])
        else:
            cisError("var doesnt exist")
        
    elif(x == "new"):
        
        if(y == "file"):
            if(os.path.exists("userfiles/" + z) == False):
                file = open("userfiles/" + z,"a")
                file.write("")
                file.close()
                
        elif(y == "folder"):
            if(os.path.exists("userfiles/" + z) == False):
                os.mkdir("userfiles/" + z)
        elif(y == "func"):
            if(os.path.exists("userfuncs/" + z) == False):
                file = open("userfiles/" + z,"a")
                file.write("")
                file.close()
        else:
            cisError("unkown file type: " + y)
        
    elif(x == "add"):
        
        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = str(FOrI(vardata[varname.index(z)]) + FOrI(vardata[varname.index(t)]))
                else:
                    varname.append(y)
                    vardata.append(str(FOrI(vardata[varname.index(z)]) + FOrI(vardata[varname.index(t)])))
            else:
                cisError("var doesnt exist")
        else:
            cisError("var doesnt exist")
        
    elif(x == "minus"):
        
        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = str(FOrI(vardata[varname.index(z)]) + FOrI(vardata[varname.index(t)]))
                else:
                    varname.append(y)
                    vardata.append(str(FOrI(vardata[varname.index(z)]) + FOrI(vardata[varname.index(t)])))
            else:
                cisError("var doesnt exist")
        else:
            cisError("var doesnt exist")
        
    elif(x == "multiply"):
        
        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = str(FOrI(vardata[varname.index(z)]) + FOrI(vardata[varname.index(t)]))
                else:
                    varname.append(y)
                    vardata.append(str(FOrI(vardata[varname.index(z)]) + FOrI(vardata[varname.index(t)])))
            else:
                cisError("var doesnt exist")
        else:
            cisError("var doesnt exist")
        
    elif(x == "divide"):

        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = str(FOrI(vardata[varname.index(z)]) + FOrI(vardata[varname.index(t)]))
                else:
                    varname.append(y)
                    vardata.append(str(FOrI(vardata[varname.index(z)]) + FOrI(vardata[varname.index(t)])))
            else:
                cisError("var doesnt exist")
        else:
            cisError("var doesnt exist")
    
    elif(x == "exponent"):

        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = str(FOrI(vardata[varname.index(z)]) + FOrI(vardata[varname.index(t)]))
                else:
                    varname.append(y)
                    vardata.append(str(FOrI(vardata[varname.index(z)]) + FOrI(vardata[varname.index(t)])))
            else:
                cisError("var doesnt exist")
        else:
            cisError("var doesnt exist")

    elif(x == "join"):

        if(t in varname):
            if(z in varname):
                if(y in varname):
                    vardata[varname.index(y)] = vardata[varname.index(z)] + vardata[varname.index(t)]
                else:
                    varname.append(y)
                    vardata.append(vardata[varname.index(z)] + vardata[varname.index(t)])
            else:
                cisError("var doesnt exist")
        else:
            cisError("var doesnt exist")
            
    elif(x == "clear"):

        if(y == "screen"):
            os.system("clear")
        elif(y == "file"):
            if(os.path.exist("userfiles/" + z)):
                with open(z,'r+') as file:
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
            cisError("file doesnt exist")

    elif(x == "child"):

        if(y == " "):
            print(os.listdir("userfiles"))
            print()
        else:
            if(os.path.exists("userfiles/" + y)):
                print(os.listdir("userfiles/" + y))
                print()
            else:
                cisError("folder doesnt exist")

    elif(x == "run"):

        if(os.path.exists("userfiles/" + y)):
            ftype = y
            fRom = ftype.split(".")
            ftype = fRom[len(fRom)-1]

            if(ftype == "cis"):
                file1 = open("userfiles/" + y, 'r')
                for line in file1:
                    compileCis(line.strip())
                file1.close()

            elif(ftype == "py"):
                os.system("python3 userfiles/" + y)
            elif(ftype == "js"):
                os.system("node userfiles/" + y)
            else:
                cisError("sorry language not supported")
        else:
            cisError("file doesnt exist")

    elif(x == "vardata"):
        print(vardata)

    elif(x == "varname"):
        print(varname)

    elif(x == "//"):
        pass

    else:
        cisError("command unrecognized " + x)

def cisError(msg):
    print("\n\033[1;31m! " + msg + " !\033[1;0m\n")

print("""dotCIS 1.3 (system32, Jan 28 2023, 9:12) 
[Powered and run by Python3] on linux
Type "help" if you are unsure what to do.
""")
while(True):
    cmdRom = input(">> ")
    cZplacement = 1
    if(cmdRom[0] == ":"):
        amountZ = cmdRom.count("z")
        for i in range(amountZ):
            cZplacement += i
        compileCis(pastCmd[len(pastCmd) - cZplacement])
    else:
        pastCmd.append(cmdRom)
        compileCis(cmdRom)