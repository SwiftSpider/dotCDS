import os.path
import os
import time
pastCmd = list([])

vardata = list([])
varname = list([])

listdata = list([])
listname = list([])
listindex = list([])

alphabet = list("abcdefghifklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
decimal = list("1234567890")
writingsys = list("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM~`!@#$%^&*()_-+={[}]|:;'<?>/")
fimgtypes = ("png", "jpeg", "ppm", "gif", "tiff","bmp","jpg","webp")
faudiotypes = ("wav","mp3","voc","au","oga","weba")
fdoctypes = ("txt","doc","docx","pdf")
fscriptypes = ("py","js","html","cs","c","c++")

global directory
directory = "DataBin/"

def getGlobeVar():
    file1 = open("VarBin.txt", 'r')
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
            if(thing[i] not in list(decimal)):
                if(thing[i] != "$"):
                    isStr = True
        if(isStr):
            #if var
            if(thing in varname):
                return vardata[varname.index(str(thing))]
            #if string
            else:
                return str(thing)
        else:
            if("$" in list(thing)):
                #if float
                if("." in list(str(thing))):
                    return float(thing.split("$")[1])
                #if int
                else:
                    return int(thing.split("$")[1])
            else:
                    #if float
                if("." in list(str(thing))):
                    return float(thing)
                #if int
                else:
                    return int(thing)
def runCmd(x,y,z,t):

    file = open("Settings.txt")
    data = list([])
    for line in file:
        data.append(line.strip())
    userPassword = dencode(data[0])
    userDesign = dencode(data[2])
    userUsername = dencode(data[1])

    if(x == "help"):
        if(y == "read"):
            print("""
""")
        elif(y == "say"):
            print("""the 'say' command writes out the contents of a value or variable.
a valid way of doing this would be
>> say thing
you would have to declare thing or give it a value before hand though
like this
>> thing = 5
>> say thing
5""")
        elif(y == "write"):
            print("""this command isnt very useful unless you forgot to add like 'wn.mainloop()' or something
the way you use this command is as so
>> write program.py print(x)
and just like that print(x) will be at the end of your code
(im sorry but you cant use tab with this or it really bugs out)
>> write program.py     print(x)""")
        elif(y == "new"):
            print("""nice and usefull 'new' creates a new folder or file for you
>> new file importantDoc.txt
a new txt file will appear although doesnt automaticly open
>> new folder favGames
a new folder named fav games will be created""")
        elif(y == "math"):
            print(""">> five = 5
will create a new variable if it doesnt already exist and change its value to five
>> six = five + 1
creates variable six if not already done so and set it to the sum of the variable 'five' and the integer '1'
which will be 6 in this case""")
        elif(y == "clear"):
            print(""">> clear file program.py
will delete all contents of the file and make it empty
>> clear folder examples
this would get rid of every file in it but im not sure about images and stuff
>> clear screen
will clear the terminal""")
        elif(y == "delete"):
            print(""">> delete file program.py
will delete the file itself and
>> delete folder examples
will delete the folder along with everything in it""")
        elif(y == "child"):
            print(""">> child
gives you the contents of the current folder...
thats it""")
        elif(y == "run"):
            print(""">> run program.py
executes the program in python
>> run program.js
executes the program in javascript
>> run program.cds
executes the program in this language
(cds can ONLY be run while using this software thing)""")
        elif(y == "varlist"):
            print(""">> varlist
for all existing variables it
gives you the name of the variable and
the value""")
        elif(y == "if"):
            print(""">> five = 5
>> if five == five say GOOD
GOOD
if five equals five then write 'GOOD'
in this case it will write 'GOOD'""")
        elif(y == "comment"):
            print(">> // this is a comment")
        elif(y == "repeat"):
            print(""">> repeat 3 say hi
hi
hi
hi
does commands or list of commands x many times
can also use variables
>> repeat three say hi""")
        elif(y == "direct"):
            print("""directory is what folder you are in
you can access files in the folder you are in
you can go into other folders by
>> open Examples""")
        elif(y == "input"):
            print(""">> input name
name person
say REPLY
person
user input and input is REPLY""") 
        elif(y == "read"):
            print(""">> bash echo "hello"
hello
bash shell commands""")
        elif(y == "wait"):
            print(""">> wait 5
this will wait 5 seconds until continuing script""")
        elif(y == "close"):
            print("""revert directory folder to the parent""")
        else:
            print("""there are many things that i could not collapse all into one letter
please specify what you want help on
a list of things i can help you with is as follows
read, say, write, new, math, clear, delete, child, run, varlist,
# if, comment, repeat, direct, input, bash, wait, close, install""")
                  
#         print("""help -gives you info of commands
# read (file) -reads the given files contents
# say (var) -writes out given variable
# write (file) (thing) -writes in a script (not recommended)
# new (type) (name) -creates new file or folder
# (var) = (value) -sets var slot to given value
# (var) = (var) (operation) (var) -math
# clear (type) (name) -clears the file/folder (if clearing screen then dont use (name)
# delete (type) (name) -deletes file/folder/image (not sure about image though)
# child -says the children of the current folder
# run (file) -run a script
# varlist -lists all var names and data
# if (var) (statement) (var) (command) -if whatever then do command
# // (comment) -system skips this command
# repeat (var) (command) -repeats command var times
# open (folder) -opens folder and changes directory
# input (question) -variable for this is REPLY
# bash (command) -input a bash command
# wait (seconds) -duh
# close -reverts to parent folder
# install (package) -installs a supported package for you
# install store -shows avialable packages

# developer tools
# system clear settings -clears and redoes settings
# system open sys -opens system file incase you want to mess with it but its already perfect :)
# system open user -opens your files for easy handleing
# system read settings -writes out current settings

# vars can be made into lists by separating values in a var with |
# duetsch = hallo|wie_gehts?
# say deutsch:0
# say duetsch:1

# global variables can also be made like this
# $fuenf = 5
# now every time you run a new instance that variable will be auto made
# you can also change them
# you can get rid of them by setting them to NULL
# $fuenf = NULL

# commands can be arranged in this format:
# thing = hello_;other = world;done = thing ++ other;say done

# two +'s joins the variables together ex.
# helloworld = hello ++ world

# :z -up arrow/goes to your last said command
# :zz -second last
# :zzz -so on""")
        
    elif(x == "read"):
        if(os.path.exists(y)):
            with open(y,'r',encoding='utf-8') as file:
                data = list(file.readlines())
            for i in range(len(data)):
                print("[" + str(i) + "] " + str(data[i]) + "\033[A")
            print()
        else:
            cdsError("file doesnt exist")
        
    elif(x == "write"):
        if(os.path.exists(y)):
            file = open(y,"a")
            file.write("\n" + z)
            file.close()
        else:
            cdsError("file doesnt exist")
        
    elif(x == "set"):
        if("$" in y):
            if(z != "NULL"):
                if(varinfile(y.split("$")[1],"VarBin.txt")):

                    #gethering file contents
                    with open('VarBin.txt','r',encoding='utf-8') as file:
                        data = list(file.readlines())
                    newData = list([])

                    #gather names of variables
                    for i in range(len(data)):
                        newData.append(data[i].split(" ")[0])
                    
                    #isolating and resetting specific variable
                    data[newData.index(y.split("$")[1])] = newData[newData.index(y.split("$")[1])] + " = " + z

                    #wipe file
                    with open("VarBin.txt",'r+') as file:
                        file.truncate(0)
                    
                    #putting list in file
                    file = open("VarBin.txt","a")
                    for i in range(len(data)):
                        file.write(data[i])
                    file.close()

                    #setting local variable
                    vardata[varname.index(y.split("$")[1])] = z
                else:

                    file = open("VarBin.txt","a")
                    file.write("\n" + y.split("$")[1] + " = " + z )
                    file.close()
                    varname.append(y.split("$")[1])
                    vardata.append(z)
            else:
                
                    #gethering file contents
                    with open('VarBin.txt','r',encoding='utf-8') as file:
                        data = list(file.readlines())
                    newData = list([])

                    #gather names of variables
                    for i in range(len(data)):
                        newData.append(data[i].split(" ")[0])
                    
                    #isolating and blanking variable space out
                    data[newData.index(y.split("$")[1])] = ""

                    #wipe file
                    with open("VarBin.txt",'r+') as file:
                        file.truncate(0)
                    
                    #putting list in file
                    file = open("VarBin.txt","a")
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
            if(os.path.exists(z) == False):
                file = open(z,"a")
                file.write("")
                file.close()
                
        elif(y == "folder"):
            if(os.path.exists(z) == False):
                os.mkdir(z)
        else:
            cdsError("unkown file type: " + y)
        
    elif(x == "add"):
        
        if(str(type(valof(t))) in ("<class 'int'>","<class 'float'>")):
            if(str(type(valof(z))) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valof(z) + valof(t))
                else:
                    varname.append(y)
                    vardata.append(str(valof(z) + valof(t)))
            else:
                cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
        else:
            cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
        
    elif(x == "minus"):
        
        if(str(type(valof(t))) in ("<class 'int'>","<class 'float'>")):
            if(str(type(valof(z))) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valof(z) - valof(t))
                else:
                    varname.append(y)
                    vardata.append(str(valof(z) - valof(t)))
            else:
                cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
        else:
            cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
        
    elif(x == "multiply"):
        
        if(str(type(valof(t))) in ("<class 'int'>","<class 'float'>")):
            if(str(type(valof(z))) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valof(z) * valof(t))
                else:
                    varname.append(y)
                    vardata.append(str(valof(z) * valof(t)))
            else:
                cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
        else:
            cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
        
    elif(x == "divide"):

        if(str(type(valof(t))) in ("<class 'int'>","<class 'float'>")):
            if(str(type(valof(z))) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valof(z) / valof(t))
                else:
                    varname.append(y)
                    vardata.append(str(valof(z) / valof(t)))
            else:
                cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
        else:
            cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
    
    elif(x == "exponent"):

        if(str(type(valof(t))) in ("<class 'int'>","<class 'float'>")):
            if(str(type(valof(z))) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valof(z) ** valof(t))
                else:
                    varname.append(y)
                    vardata.append(str(valof(z) ** valof(t)))
            else:
                cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
        else:
            cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])

    elif(x == "join"):

        if(str(type(valof(t))) in ("<class 'int'>","<class 'float'>")):
            if(str(type(valof(z))) in ("<class 'int'>","<class 'float'>")):
                if(y in varname):
                    vardata[varname.index(y)] = str(valof(z)) + str(valof(t))
                else:
                    varname.append(y)
                    vardata.append(str(valof(z)) + str(valof(t)))
            else:
                cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
        else:
            cdsError("cannot do math with var type " + str(type(valof(z))).split("'")[1])
            
    elif(x == "clear"):

        if(y == "screen"):
            os.system("clear")
        elif(y == "file"):
            if(os.path.exists(z)):
                with open(z,'r+') as file:
                    file.truncate(0)
        elif(y == "folder"):
            listdir = os.listdir(z)
            for i in range(len(os.listdir(z))):
                os.remove(z + "/" + listdir[i])
        
    elif(x == "delete"):
        
        if(os.path.exists(z)):
            if(y in ("file","image")):
                os.remove(z)
            elif(y == "folder"):
                if(len(os.listdir(z)) == 0):
                    os.rmdir(z)
                else:
                    listdir = os.listdir(z)
                    for i in range(len(os.listdir(z))):
                        os.remove(z + "/" + listdir[i])
                    os.rmdir(z)
        else:
            cdsError("file doesnt exist")

    elif(x == "child"):
        romlist = list(os.listdir(directory))
        for i in range(len(romlist)):
            if("." in list(romlist[i])):
                if(romlist[i].split(".")[len(romlist[i].split("."))-1] in fimgtypes):
                    print("[" + str(i) + "]|i| " + romlist[i])
                elif(romlist[i].split(".")[len(romlist[i].split("."))-1] in fscriptypes):
                    print("[" + str(i) + "]|s| " + romlist[i])
                elif(romlist[i].split(".")[len(romlist[i].split("."))-1] in faudiotypes):
                    print("[" + str(i) + "]|a| " + romlist[i])
                elif(romlist[i].split(".")[len(romlist[i].split("."))-1] in fdoctypes):
                    print("[" + str(i) + "]|d| " + romlist[i])
            else:
                print("[" + str(i) + "]|f| " + romlist[i])

    elif(x == "run"):
        if(os.path.exists(y)):
            ftype = y
            fRom = ftype.split(".")
            ftype = fRom[len(fRom)-1]

            if(ftype == "cds"):
                file1 = open(y, 'r')
                for line in file1:
                    linestrip = line.strip()
                    for i in range(len(linestrip.split(";"))):
                        if(linestrip.split(";")[i] != ""):
                            compilecds(linestrip.split(";")[i])
                file1.close()

            elif(ftype == "py"):
                os.system("python3 " + y)
            elif(ftype == "js"):
                os.system("node " + y)
            else:
                cdsError("sorry language not supported")
        else:
            children = list(os.listdir())
            for i in range(len(children)):
                if(len(children[i]) <= y):
                    del children[i]
            for i in range(len(y)):
                for x in range(len(children)):
                    if(y[i] != children[x][i]):
                        del children[x]
            if(len(children) != 0):
                ftype = children[0]
                fRom = ftype.split(".")
                ftype = fRom[len(fRom)-1]

                if(ftype == "cds"):
                    file1 = open(children[0], 'r')
                    for line in file1:
                        linestrip = line.strip()
                        for i in range(len(linestrip.split(";"))):
                            if(linestrip.split(";")[i] != ""):
                                compilecds(linestrip.split(";")[i])
                    file1.close()

                elif(ftype == "py"):
                    os.system("python3 " + children[0])
                elif(ftype == "js"):
                    os.system("node " + children[0])
                else:
                    cdsError("sorry language not supported")
            else:
                cdsError("path does not exist")

    elif(x == "varlist"):
        
        for i in range(len(varname)):
            print("[" + str(i) + "] " + varname[i] + " : " + vardata[i])

    elif(x == "//"):
        pass
    
    elif(x == "ifeq"):
        if(valof(y) == valof(z)):
            for i in range(len(t.split(";"))):
                if(t.split(";")[i] != ""):
                    compilecds(t.split(";")[i])
    elif(x == "ifgt"):
        if(str(type(valof(y))) in ("<class 'int'>","<class 'float'>")):
            if(str(type(valof(z))) in ("<class 'int'>","<class 'float'>")):
                if(valof(y) > valof(z)):
                    for i in range(len(t.split(";"))):
                        if(t.split(";")[i] != ""):
                            compilecds(t.split(";")[i])
            else:
                cdsError("cannot use in statement " + type(valof(z)).split("'")[1])
        else:
            cdsError("cannot use in statement " + type(valof(y)).split("'")[1])
    elif(x == "iflt"):
        if(str(type(valof(y))) in ("<class 'int'>","<class 'float'>")):
            if(str(type(valof(z))) in ("<class 'int'>","<class 'float'>")):
                if(valof(y) < valof(z)):
                    for i in range(len(t.split(";"))):
                        if(t.split(";")[i] != ""):
                            compilecds(t.split(";")[i])
            else:
                cdsError("cannot use in statement " + type(valof(z)).split("'")[1])
        else:
            cdsError("cannot use in statement " + type(valof(y)).split("'")[1])
    elif(x == "ifge"):
        if(str(type(valof(y))) in ("<class 'int'>","<class 'float'>")):
            if(str(type(valof(z))) in ("<class 'int'>","<class 'float'>")):
                if(valof(y) >= valof(z)):
                    for i in range(len(t.split(";"))):
                        if(t.split(";")[i] != ""):
                            compilecds(t.split(";")[i])
            else:
                cdsError("cannot use in statement " + type(valof(z)).split("'")[1])
        else:
            cdsError("cannot use in statement " + type(valof(y)).split("'")[1])
    elif(x == "ifle"):
        if(str(type(valof(y))) in ("<class 'int'>","<class 'float'>")):
            if(str(type(valof(z))) in ("<class 'int'>","<class 'float'>")):
                if(valof(y) <= valof(z)):
                    for i in range(len(t.split(";"))):
                        if(t.split(";")[i] != ""):
                            compilecds(t.split(";")[i])
            else:
                cdsError("cannot use in statement " + type(valof(z)).split("'")[1])
        else:
            cdsError("cannot use in statement " + type(valof(y)).split("'")[1])
    elif(x == "ifne"):
        if(valof(vardata[varname.index(y)],False) != valof(vardata[varname.index(y)],False)):
            for i in range(len(t.split(";"))):
                if(t.split(";")[i] != ""):
                    compilecds(t.split(";")[i])
    
    elif(x == "input"):
        vardata[varname.index("REPLY")] = input(y)
        for i in range(len(str(t).split(";"))):
            if(str(t).split(";")[i] != ""):
                compilecds(str(t).split(";")[i])
    
    elif(x == "repeat"):
        if(type(valof(y)) == type(5)):
            for i in range(valof(y)):
                for i in range(len(z.split(";"))):
                    if(z.split(";")[i] != ""):
                        compilecds(z.split(";")[i])
        else:
            cdsError("invalid input type")
    elif(x == "open"):
        if(y[len(y)-1] == "/"):
            if(os.path.exists(y)):
                dirChange(y)
                os.system("cd " + y)
            else:
                children = list(os.listdir())
                for i in range(len(children)):
                    if(len(children[i]) <= y):
                        del children[i]
                for i in range(len(y)):
                    for x in range(len(children)):
                        if(y[i] != children[x][i]):
                            del children[x]
                if(len(children) != 0):
                    dirChange(children[0])
                    os.system("cd " + children[0])
                else:
                    cdsError("path does not exist")
        else:
            if(os.path.exists(y + "/")):
                dirChange(y + "/")
            else:
                cdsError("path does not exist")
    elif(x == "close"):
        if(directory != "DataBin/"):
            dirChange(directory.split(directory.split("/")[len(directory.split("/"))-2])[0])
            os.system("cd ..")
    elif(x == "sleep"):
        time.sleep(valof(y))
    elif(x == "append"):
        vardata[varname.index(y)] += "|" + z
    elif(x == "system"):
        if(y == "open"):
            if(z == "sys"):
                password = input("Password: ")
                if(password == userPassword):
                    os.system("code System.py")
            elif(z == "user"):
                password = input("Password: ")
                if(password == userPassword):
                    os.system("code DataBin")
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
                    file = open("Settings.txt","a")
                    file.truncate(0)
                    startup()
                    file = open("Settings.txt", 'r')
                    data = list([])
                    for line in file:
                        if(line.strip() != ""):
                            data.append(line.strip())
                    userPassword = dencode(data[0])
                    userUsername = dencode(data[1])
                    userDesign = dencode(data[2])
    elif(x == "bash"):
        os.system(y)
    elif(x == "install"):
        print("download will begin shortly, please type 'y' to any (Y/N) questions\n")
        time.sleep(3)
        if(y in ("tkinter","tk")):
            os.system("sudo apt-get update")
            os.system("sudo apt-get upgrade")
            os.system("sudo apt-get install python3-tk")
        elif(y in ("vscode","vs","code","visualstudio")):
            os.system("sudo apt update")
            os.system("sudo apt upgrade")
            os.system("sudo apt install code")
        elif(y in ("git","github")):
            os.system("sudo apt update")
            os.system("sudo apt upgrade")
            os.system("sudo apt install git")
        elif(y in ("node","js","javascript","nodejs","nodejavascript")):
            os.system("sudo apt update")
            os.system("sudo apt upgrade")
            os.system("sudo apt install nodejs")
            os.system("sudo apt install npm")
        elif(y == "pygame"):
            os.system("python3 -m pip install -U pygame==2.1.3 --user")
        elif(y in ("pip","pip3")):
            os.system("sudo apt-get update")
            os.system("sudo apt-get upgrade")
            os.system("sudo apt-get install python3-pip")
        elif(y in ("pil","pillow")):
            os.system("python3 -m pip install pillow")
        elif(y in ("full","package","all")):
            os.system("sudo apt update")
            os.system("sudo apt upgrade")
            os.system("sudo apt-get update")
            os.system("sudo apt-get upgrade")
            os.system("sudo apt-get install python3-pip")
            os.system("python3 -m pip install pillow")
            os.system("python3 -m pip install -U pygame==2.1.3 --user")
            os.system("sudo apt install nodejs")
            os.system("sudp apt install npm")
            os.system("sudo apt-get install python3-tk")
            os.system("sudo apt install code")
            os.system("sudo apt install git")
            print("\nJAVASCRIPT VERSION")
            os.system("node -v")
            os.system("npm -v")
            print("\nPIP VERSION")
            os.system("pip -v")
            print()
        elif(y in ("available","store","catalog")):
            print("Pip\nGithub\nVSCode\nTkinter\nJavaScript\nPillow\n")
        else:
            cdsError("unknown program")
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
    file = open("Settings.txt", 'r')
    data = list([])
    for line in file:
        if(line.strip() != ""):
            data.append(line.strip())
    file = open("Settings.txt", 'a')
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
file = open("Settings.txt", 'r')
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
    # dev@dotCDS:~DataBin/: >> _
    if(userDesign == "linux"):
        if(directory == "DataBin/"):
            cmdRom = input("\033[1;32m" + userUsername + "@penguin:\033[1;34m~" + directory.split("DataBin/")[1] + "\033[1;0m$ ")
        else:
            cmdRom = input("\033[1;32m" + userUsername + "@penguin:\033[1;34m~/" + directory.split("DataBin/")[1] + "\033[1;0m$ ")
    elif(userDesign == "windows"):
        cmdRom = input("\033[1;37mC:\u005cUsers\u005c" + userUsername + "\u005c" + directory.split("DataBin/")[1] + ">")
    else:
        cmdRom = input(userUsername + ": " + directory.split("DataBin/")[1] + " >> ")
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
