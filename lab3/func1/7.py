def check(l):
    x=0
    for x in range (len(l)-1):
        if l[x+1]==3 and l[x]==3:
            k= True
            break
        else:
            k= False
    return k
    
    
    
my_list=list(map(int, input().split()))
print (check(my_list))