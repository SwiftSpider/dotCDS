import time
import random
alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
while True:
    code = ""
    for i in range(15):
        code += alphabet[random.randint(0,len(alphabet)-1)]
    print("\033[1;31m[" + code + "|0.00btc|$0.00]")
    time.sleep(0.02)