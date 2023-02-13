import os.path
import os
import time

pastCmd = list([])

vardata = list([])
varname = list([])

listdata = list([])
listname = list([])
listindex = list([])

badChar = ("{\}|/~`[] ")
alphabet = ("abcdefghifklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
decimal = ("0","1","2","3","4","5","6","7","8","9")
writingsys = list("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")

global directory
directory = "userfiles/"

def valOf(input):
    for i in range(len(input)):
        if(input[i] in badChar):
            cdsError("Character not allowed " + input[i])
        else:
            if(input[i] in alphabet):
                if(input in varname):
                    return vardata[varname.index(input)]
                else:
                    return input
    if("." in input):
        return float(input)
    else:
        return int(input)
            

def getGlobeVar():
    file1 = open("globalvar", 'r')
    data = list([])
    for line in file1:
        if(line.strip() != ""):
            data.append(line.strip())
    
    for i in range(len(data)):
        compilecds(data[i])
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
        runPar[2] = cmdPar[2]
        for i in range(len(cmdPar) - 3):
            runPar[2] += " " + cmdPar[i + 3]
    elif(cmdPar[0] == "input"):
        runPar[1] = cmdPar[1]
        for i in range(len(cmdPar) - 2):
            runPar[1] += " " + cmdPar[i + 2]
    elif(cmdPar[0] == "bash"):
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
        runPar[2] = cmdPar[2]
        for i in range(len(cmdPar) - 3):
            runPar[2] += " " + cmdPar[i + 3]
    runCmd(runPar[0], runPar[1], runPar[2], runPar[3])

def valof(thing):
    #if list
    if(":" in thing):
        return vardata[int(varname.index(thing.split(":")[0]))].split("|")[int(thing.split(":")[1])]
    else:
        isStr = False
        for i in range(len(str(thing))):
            if(thing[i] in list(alphabet)):
                isStr = True
        if(isStr):
            #if var
            if(thing in varname):
                return vardata[varname.index(str(thing))]
            #if string
            else:
                return str(thing)
        else:
            #if float
            if("." in list(str(thing))):
                return float(thing)
            #if int
            else:
                return int(thing)
def runCmd(x,y,z,t):

    file = open("usersettings")
    data = list([])
    for line in file:
        data.append(line.strip())
    userPassword = dencode(data[0])
    userDesign = dencode(data[2])
    userUsername = dencode(data[1])

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
open (folder) -opens folder and changes directory
input (question) -variable for this is REPLY
bash (command) -input a bash command
wait (seconds) -duh
close -reverts to parent folder

developer tools
system clear settings -clears and redoes settings
system open sys -opens system file incase you want to mess with it but its already perfect :)
system open user -opens your files for easy handleing
system read settings -writes out current settings

vars can be made into lists by separating values in a var with |
duetsch = hallo|wie_gehts?
say deutsch:0
say duetsch:1

global variables can also be made like this
$fuenf = 5
now every time you run a new instance that variable will be auto made
you can also change them
you can get rid of them by setting them to NULL
$fuenf = NULL

commands can be arranged in this format:
thing = hello_;other = world;done = thing ++ other;say done

two +'s joins the variables together ex.
helloworld = hello ++ world

:z -up arrow/goes to your last said command
:zz -second last
:zzz -so on""")
        
    elif(x == "read"):
        if(os.path.exists(directory + y)):
            with open(directory + y,'r',encoding='utf-8') as file:
                data = list(file.readlines())
            for i in range(len(data)):
                print("[" + str(i) + "] " + str(data[i]) + "\033[A")
            print()
        else:
            cdsError("file doesnt exist")
        
    elif(x == "write"):
        if(os.path.exists(directory + y)):
            file = open(directory + y,"a")
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
            if(":" in y):
                data = vardata[varname.index(y.split(":")[0])].split("|")
                data[int(y.split(":")[1])] = z
                rom = data[0]
                for i in range(len(data)-1):
                    rom += "|" + data[i+1]
                vardata[varname.index(y.split(":")[0])] = rom
            elif(y in varname):
                vardata[varname.index(y)] = z
            else:
                varname.append(y)
                vardata.append(z)
        
    elif(x == "say"):
        if(y == ''):
            print()
        else:
            print(valof(y))
        
    elif(x == "new"):
        
        if(y == "file"):
            if(os.path.exists(directory + z) == False):
                file = open(directory + z,"a")
                file.write("")
                file.close()
                
        elif(y == "folder"):
            if(os.path.exists(directory + z) == False):
                os.mkdir(directory + z)
        else:
            cdsError("unkown file type: " + y)
        
    elif(x == "add"):
        
        if(type(valOf(t)) in ("<class 'int'>","<class 'float'>")):
            if(type(valOf(z)) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valOf(z) + valOf(t))
                else:
                    varname.append(y)
                    vardata.append(str(valOf(z) + valOf(t)))
            else:
                cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
        else:
            cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
        
    elif(x == "minus"):
        
        if(type(valOf(t)) in ("<class 'int'>","<class 'float'>")):
            if(type(valOf(z)) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valOf(z) - valOf(t))
                else:
                    varname.append(y)
                    vardata.append(str(valOf(z) - valOf(t)))
            else:
                cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
        else:
            cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
        
    elif(x == "multiply"):
        
        if(type(valOf(t)) in ("<class 'int'>","<class 'float'>")):
            if(type(valOf(z)) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valOf(z) * valOf(t))
                else:
                    varname.append(y)
                    vardata.append(str(valOf(z) * valOf(t)))
            else:
                cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
        else:
            cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
        
    elif(x == "divide"):

        if(type(valOf(t)) in ("<class 'int'>","<class 'float'>")):
            if(type(valOf(z)) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valOf(z) / valOf(t))
                else:
                    varname.append(y)
                    vardata.append(str(valOf(z) / valOf(t)))
            else:
                cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
        else:
            cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
    
    elif(x == "exponent"):

        if(type(valOf(t)) in ("<class 'int'>","<class 'float'>")):
            if(type(valOf(z)) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valOf(z) ** valOf(t))
                else:
                    varname.append(y)
                    vardata.append(str(valOf(z) ** valOf(t)))
            else:
                cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
        else:
            cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])

    elif(x == "join"):

        if(type(valOf(t)) in ("<class 'int'>","<class 'float'>")):
            if(type(valOf(z)) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valOf(z)) + str(valOf(t))
                else:
                    varname.append(y)
                    vardata.append(str(valOf(z)) + str(valOf(t)))
            else:
                cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
        else:
            cdsError("cannot do math with var type " + type(valOf(z)).split("'")[1])
            
    elif(x == "clear"):

        if(y == "screen"):
            os.system("clear")
        elif(y == "file"):
            if(os.path.exists(directory + z)):
                with open(directory + z,'r+') as file:
                    file.truncate(0)
        elif(y == "folder"):
            listdir = os.listdir(directory + z)
            for i in range(len(os.listdir(directory + z))):
                os.remove(directory + z + "/" + listdir[i])
        
    elif(x == "delete"):
        
        if(os.path.exists(directory + z)):
            if(y == "file"):
                os.remove(directory + z)
            elif(y == "folder"):
                if(len(os.listdir(directory + z)) == 0):
                    os.rmdir(directory + z)
                else:
                    listdir = os.listdir(directory + z)
                    for i in range(len(os.listdir(directory + z))):
                        os.remove(directory + z + "/" + listdir[i])
                    os.rmdir(directory + z)
        else:
            cdsError("file doesnt exist")

    elif(x == "child"):
        romlist = list(os.listdir(directory))
        for i in range(len(romlist)):
            if("." in list(romlist[i])):
                print("[" + str(i) + "]|s| " + romlist[i])
            else:
                print("[" + str(i) + "]|f| " + romlist[i])

    elif(x == "run"):

        if(os.path.exists(directory + y)):
            ftype = y
            fRom = ftype.split(".")
            ftype = fRom[len(fRom)-1]

            if(ftype == "cds"):
                file1 = open(directory + y, 'r')
                for line in file1:
                    linestrip = line.strip()
                    for i in range(len(linestrip.split(";"))):
                        if(linestrip.split(";")[i] != ""):
                            compilecds(linestrip.split(";")[i])
                file1.close()

            elif(ftype == "py"):
                os.system("python3 " + directory + y)
            elif(ftype == "js"):
                os.system("node " + directory + y)
            else:
                cdsError("sorry language not supported")
        else:
            cdsError("file doesnt exist")

    elif(x == "varlist"):
        
        for i in range(len(varname)):
            print("[" + str(i) + "] " + varname[i] + " : " + vardata[i])

    elif(x == "//"):
        pass
    
    elif(x == "ifeq"):
        if(valof(y) == valOf(z)):
            for i in range(len(t.split(";"))):
                if(t.split(";")[i] != ""):
                    compilecds(t.split(";")[i])
    elif(x == "ifgt"):
        if(type(valof(y)) in ("<class 'int'>","<class 'float'>")):
            if(type(valof(z)) in ("<class 'int'>","<class 'float'>")):
                if(valof(y) > valOf(z)):
                    for i in range(len(t.split(";"))):
                        if(t.split(";")[i] != ""):
                            compilecds(t.split(";")[i])
            else:
                cdsError("cannot use in statement " + type(valof(z)).split("'")[1])
        else:
            cdsError("cannot use in statement " + type(valof(y)).split("'")[1])
    elif(x == "iflt"):
        if(type(valof(y)) in ("<class 'int'>","<class 'float'>")):
            if(type(valof(z)) in ("<class 'int'>","<class 'float'>")):
                if(valof(y) < valOf(z)):
                    for i in range(len(t.split(";"))):
                        if(t.split(";")[i] != ""):
                            compilecds(t.split(";")[i])
            else:
                cdsError("cannot use in statement " + type(valof(z)).split("'")[1])
        else:
            cdsError("cannot use in statement " + type(valof(y)).split("'")[1])
    elif(x == "ifge"):
        if(type(valof(y)) in ("<class 'int'>","<class 'float'>")):
            if(type(valof(z)) in ("<class 'int'>","<class 'float'>")):
                if(valof(y) >= valOf(z)):
                    for i in range(len(t.split(";"))):
                        if(t.split(";")[i] != ""):
                            compilecds(t.split(";")[i])
            else:
                cdsError("cannot use in statement " + type(valof(z)).split("'")[1])
        else:
            cdsError("cannot use in statement " + type(valof(y)).split("'")[1])
    elif(x == "ifle"):
        if(type(valof(y)) in ("<class 'int'>","<class 'float'>")):
            if(type(valof(z)) in ("<class 'int'>","<class 'float'>")):
                if(valof(y) <= valOf(z)):
                    for i in range(len(t.split(";"))):
                        if(t.split(";")[i] != ""):
                            compilecds(t.split(";")[i])
            else:
                cdsError("cannot use in statement " + type(valof(z)).split("'")[1])
        else:
            cdsError("cannot use in statement " + type(valof(y)).split("'")[1])
    elif(x == "ifne"):
        if(FOrI(vardata[varname.index(y)],False) != FOrI(vardata[varname.index(y)],False)):
            for i in range(len(t.split(";"))):
                if(t.split(";")[i] != ""):
                    compilecds(t.split(";")[i])
    
    elif(x == "input"):
        vardata[varname.index("REPLY")] = input(y)
        for i in range(len(str(t).split(";"))):
            if(str(t).split(";")[i] != ""):
                compilecds(str(t).split(";")[i])
    
    elif(x == "repeat"):
        if(type(valOf(y)) == type(5)):
            for i in range(valOf(y)):
                for i in range(len(z.split(";"))):
                    if(z.split(";")[i] != ""):
                        compilecds(z.split(";")[i])
        else:
            cdsError("invalid input type")
    elif(x == "open"):
        if(y[len(y)-1] == "/"):
            if(os.path.exists(directory + y)):
                dirChange(directory + y)
            else:
                cdsError("path does not exist")
        else:
            if(os.path.exists(directory + y + "/")):
                dirChange(directory + y + "/")
            else:
                cdsError("path does not exist")
    elif(x == "close"):
        if(directory != "userfiles/"):
            dirChange(directory.split(directory.split("/")[len(directory.split("/"))-2])[0])
    elif(x == "sleep"):
        time.sleep(valof(y))
    elif(x == "append"):
        vardata[varname.index(y)] += "|" + z
    elif(x == "system"):
        if(y == "open"):
            if(z == "sys"):
                password = input("Password: ")
                if(password == userPassword):
                    os.system("code system32.py")
            elif(z == "user"):
                password = input("Password: ")
                if(password == userPassword):
                    os.system("code userfiles")
        elif(y == "read"):
            if(z == "settings"):
                password = input("Password: ")
                if(password == userPassword):
                    print()
                    print("Username : " + userUsername)
                    print("Password : " + userPassword)
                    print("Theme    : " + userDesign)
        elif(y == "clear"):
            if(z == "settings"):
                password = input("Password: ")
                if(password == userPassword):
                    file = open("usersettings","a")
                    file.truncate(0)
                    startup()
                    file = open("usersettings", 'r')
                    data = list([])
                    for line in file:
                        if(line.strip() != ""):
                            data.append(line.strip())
                    userPassword = dencode(data[0])
                    userUsername = dencode(data[1])
                    userDesign = dencode(data[2])
    elif(x == "bash"):
        os.system(y)
    else:
        cdsError("command unrecognized " + x)

def cdsError(msg):
    if(userDesign != "windows"):
        print("\n\033[1;31m! " + msg + " !\033[1;0m\n")
    else:
        print("\n\033[1;31m! " + msg + " !\033[1;37m\n")

def debug(thing):
    print(thing)

def dirChange(newDir):
    global directory
    directory = str(newDir)

def dencode(msg):
    Return = list("")
    for i in range(len(list(msg))):
        Return.append(writingsys[int(len(writingsys) - 1 - writingsys.index(list(msg)[i]))])
    return "".join(Return)

def startup():
    file = open("usersettings", 'r')
    data = list([])
    for line in file:
        if(line.strip() != ""):
            data.append(line.strip())
    file = open("usersettings", 'a')
    if(data == list([])):
        print("looks like its your first time here!")

        def passwordset():
            password = input("please make a password: ")
            print("you selected '" + password + "' as your password")
            yep = input("correct? (Y/N) >")
            if(yep in ("y","Y")):
                file.write(dencode(password))
                userPassword = password
            elif(yep in ("n","N")):
                passwordset()
            else:
                cdsError("unknown input")
                passwordset()
        def usernameset():
            username = input("please make a username: ")
            print("you selected '" + username + "' as your username")
            yep = input("correct? (Y/N) >")
            if(yep in ("y","Y")):
                file.write("\n" + dencode(username))
                userUsername = username
            elif(yep in ("n","N")):
                usernameset()
            else:
                cdsError("unknown input")
                usernameset()
        def bashset():
            likebash = input("do you want dotCDS to look like linux terminal? (Y/N): ")
            if(likebash in ("y","Y")):
                file.write("\n" + dencode("linux"))
                userDesign = "linux"
            elif(likebash in ("n","N")):
                likewindow = input("do you want dotCDS to look like windows terminal? (Y/N): ")
                if(likewindow in ("y","Y")):
                    file.write("\n" + dencode("windows"))
                    userDesign = "windows"
                elif(likewindow in ("n","N")):
                    likenorm = input("do you want dotCDS's default look? (Y/N): ")
                    if(likenorm in ("y","Y")):
                        file.write("\n" + dencode("default"))
                        userDesign = "default"
                    elif(likenorm in ("n","N")):
                        bashset()
                    else:
                        cdsError("unknown input")
                        bashset()
                else:
                    cdsError("unknown input")
                    bashset()
            else:
                cdsError("unknown input")
                bashset()

        passwordset()
        usernameset()
        bashset()

        print("thats it! off you go now")
        time.sleep(2)
        os.system("clear")
    else:
        userPassword = dencode(data[0])
        userUsername = dencode(data[1])
        userDesign = dencode(data[2])
    file.close()
startup()
file = open("usersettings", 'r')
data = list([])
for line in file:
    if(line.strip() != ""):
        data.append(line.strip())
userPassword = dencode(data[0])
userUsername = dencode(data[1])
userDesign = dencode(data[2])

getGlobeVar()
if(userDesign == "windows"):
    print("""\033[1;37mdotCDS 1.0 (system32, Jan 28 2023, 9:12)
[Powered and run by Python3] on linux
Type "help" if you are unsure what to do.""")
else:
    print("""dotCDS 1.0 (system32, Jan 28 2023, 9:12)
[Powered and run by Python3] on linux
Type "help" if you are unsure what to do.""")
print("Hello " + userUsername)

while(True):
    # dev@dotCDS:~userfiles/: >> _
    if(userDesign == "linux"):
        if(directory == "userfiles/"):
            cmdRom = input("\033[1;32m" + userUsername + "@penguin:\033[1;34m~" + directory.split("userfiles/")[1] + "\033[1;0m$ ")
        else:
            cmdRom = input("\033[1;32m" + userUsername + "@penguin:\033[1;34m~/" + directory.split("userfiles/")[1] + "\033[1;0m$ ")
    elif(userDesign == "windows"):
        cmdRom = input("\033[1;37mC:\u005cUsers\u005c" + userUsername + "\u005c" + directory.split("userfiles/")[1] + ">")
    else:
        cmdRom = input(userUsername + ": " + directory.split("userfiles/")[1] + " >> ")
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