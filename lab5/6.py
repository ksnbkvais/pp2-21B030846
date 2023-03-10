import re
s=str(input())

x=re.sub("[ .,]" , ":", s)
print(x)