def unique(l):
    a=[]
    for i in l:
        if i not in a:
            a.append(i)
    print(list(a))

l=list(map(int,input().split()))
unique(l)