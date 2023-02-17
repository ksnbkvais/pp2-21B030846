def p(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
        else:
            return True

s=str(input())
if p(s): 
    print("yes")
else: 
    print("no")