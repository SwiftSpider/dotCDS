engAlphabetL = ("abcdefghifklmnopqrstuvwxyz ~!@#$%^&*()_+`1234567890-=[]|:;'<,>.?/")
engAlphabetC = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
sgAlphabet = ("ᔑʖᓵ↸ᒷ⎓⊣⍑╎⋮ꖌꖎᒲリ𝙹!¡ᑑ∷ᓭℸ ̣ ⚍⍊∴ ̇/||⨅ ~!@#$%^&*()_+`1234567890-=[]|:;'<,>.?/")
print()
enOrDe = input("encode or decode? >>")
msg = input(enOrDe + " >>")
result = ""
if(enOrDe[0] == "e"):
    for i in range(len(msg)):
        if(msg[i] in engAlphabetL):
            result += sgAlphabet[engAlphabetL.index(msg[i])]
        elif(msg[i] in engAlphabetC):
            result += sgAlphabet[engAlphabetC.index(msg[i])]
        else:
            print("character not allowed: " + msg[i])
            break
elif(enOrDe[0] == "d"):
    for i in range(len(msg)):
        if(msg[i] in sgAlphabet):
            result += engAlphabetL[sgAlphabet.index(msg[i])]
        else:
            print("character not allowed: " + msg[i])
            break
print()
print(result)
print()