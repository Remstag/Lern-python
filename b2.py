import math
import re
n=input()
for _ in range(int(n)):
    a=sorted([int(i) for i in re.split("[a-z]+",input()) if i!=''])
    if(len(a)>0) :print(a[-1])
