import re
s=str(input())
x='a.*?b$' 

if re.search(x, s):  
    print("match")
else: print("no match")