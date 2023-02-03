import random
import math
import time

def say(text, color):
    if (color == "gray"):
        print("\033[1;30m\n")
    elif (color == "red"):
        print("\033[1;31m\n")
    elif (color == "green"):
        print("\033[1;32m\n")
    elif (color == "yellow"):
        print("\033[1;33m\n")
    elif (color == "blue"):
        print("\033[1;34m\n")
    elif (color == "purple"):
        print("\033[1;35m\n")
    elif (color == "cyan"):
        print("\033[1;36m\n")
    elif (color == "white"):
        print("\033[1;37m\n")
    elif (color == "norm"):
        print("\033[1;0m\n")
    print(text)

def buffer(x):  # Must buffer OVER 1 line
    print("\033[1;0m\n")
    for i in range(x - 2):
        print("")

def wait(x):
    time.sleep(x)

def randLib():
    rom = charLib[random.randint(0,len(charLib)-1)]
    for i in range(lenID - 1):
        rom += charLib[random.randint(0,len(charLib)-1)]
    return rom
def cmdMenu():
    say("","norm")
    cmd = input("user@penguin:~/WalletMiner$ ")
    if(cmd == "run"):
        wait(3)
        say("Setting up Wallet Miner...","white")
        wait(4)
        directory = "wallets.txt"
        print("Directory >wallets.txt")
        wait(1)
        print("Importing")
        file1 = open("wallets.txt", "a")
        file1.write("--NEW SESSION--\n")
        file1.close()
        btcValue = 22998.30
        btcFound = 0

        lenID = 30 #length of the sequence

        alphabet = ["a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        capitalAlphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        number = ["0","1","2","3","4","5","6","7","8","9"]
        charLib = ["a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        wait(2.5)
        print("Starting Wallet Miner")
        wait(1.5)

        while( 1 != 10):

            # fails
            say("| " + randLib() + " | 0.000BTC | $0.00 |","red")
            for i in range(random.randint(1,5) * 5000):
                print("| " + randLib() + " | 0.000BTC | $0.00 |")
                wait(0.01)
    
            # bitcoin found
            btcFound = float(random.randint(10,150)) / 1000
            success = "| " + randLib() + " | " + str(btcFound) + "BTC | $" + str( math.floor((btcFound * btcValue) * 100) / 100) + " |"
            say(success ,"green")

            # upload bitcoin to directory, i dont know what the "a" means
            file1 = open("wallets.txt", "a")
            file1.write(success + "\n")
            file1.close()
            wait(6)
    elif(cmd == "list"):
        file = open("wallets.txt")
        say(file.read(),"white")
        file.close()
    elif(cmd == "clear"):
        with open("wallets.txt",'r+') as file:
            file.truncate(0)
        say("Cleared wallets.txt")

# https://www.messletters.com/en/big-text/
logo = """                8 8        w                w                     .d88b.   d88b 
Yb  db  dP .d88 8 8 .d88b w8ww    8d8b.d8b. w 8d8b. .d88b 8d8b    8P  Y8    wwP 
 YbdPYbdP  8  8 8 8 8.dP'  8      8P Y8P Y8 8 8P Y8 8.dP' 8P      8b  d8      8 
  YP  YP   `Y88 8 8 `Y88P  Y8P    8   8   8 8 8   8 `Y88P 8       `Y88P' w Y88P """
say(logo,"blue")
print("")
print("     powerd by Igra SoftWare")
say("""run -runs the wallet min
stop -stops the program
list -shows all successful wallets
clear -clears list of wallets
total -total bitcoin found""","white")
wait(1)


while(1 != 10):
    say("","norm")
    cmd = input(">>> ")
    if(cmd == "run"):
        wait(3)
        say("Setting up Wallet Miner...","white")
        wait(4)
        directory = "wallets.txt"
        print("Directory >wallets.txt")
        wait(1)
        print("Importing")
        file1 = open("wallets.txt", "a")
        file1.write("--NEW SESSION--\n")
        file1.close()
        btcValue = 22998.30
        btcFound = 0

        lenID = 30 #length of the sequence

        alphabet = ["a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        capitalAlphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        number = ["0","1","2","3","4","5","6","7","8","9"]
        charLib = ["a","b","c","d","e","f","g","h","i","j","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        wait(2.5)
        print("Starting Wallet Miner")
        wait(1.5)

        while( 1 != 10):

            # fails
            say("| " + randLib() + " | 0.000BTC | $0.00 |","red")
            for i in range(random.randint(1,5) * 5000):
                print("| " + randLib() + " | 0.000BTC | $0.00 |")
                wait(0.01)
    
            # bitcoin found
            btcFound = float(random.randint(10,150)) / 1000
            success = "| " + randLib() + " | " + str(btcFound) + "BTC | $" + str( math.floor((btcFound * btcValue) * 100) / 100) + " |"
            say(success ,"green")

            # upload bitcoin to directory, i dont know what the "a" means
            file1 = open("wallets.txt", "a")
            file1.write(success + "\n")
            file1.close()
            wait(6)
    elif(cmd == "list"):
        file = open("wallets.txt")
        say(file.read(),"white")
        file.close()
    elif(cmd == "clear"):
        with open("wallets.txt",'r+') as file:
            file.truncate(0)
        say("Cleared wallets.txt","white")
    elif(cmd == "total"):

        if(file.read() == ""):
            say("no bitcoin mined","white")
        else:

            file = open("total.txt")
            romTotal = file.read()
            file.close()
            with open("total.txt",'r+') as file:
                file.truncate(0)

            file1 = open("total.txt", "a")
            file1.write(btcFound + float(romTotal) + "\n")
            file1.close()