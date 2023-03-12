winput = input("paragraph >> ")
while True:
    if(winput != "stop"):
        print("\nThere are " + str(len(winput.split(".")) + len(winput.split("?")) + len(winput.split("!")) - 2) + " sentences")
        print("There are " + str(len(winput.split("'"))-1) + " '")
        print("There are " + str(len(winput.split(" "))) + " words\n")
        winput = input("paragraph >> ")
    else:
        quit()