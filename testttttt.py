bang={
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25
}
s=input()
for i in range(25):

    for j in range(len(s)):
        d = 0
        if(s[j]!='_'):
            tt=bang.get(s[j])-i
            d=1
            if(tt<0): tt+=26
        key=next((k for k,v in bang.items() if int(v)==int(tt)),None)
        if(d==1): print(key,end="")
        else : print(s[j],end="")
    print(" ",i)