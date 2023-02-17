def histogram(a):
    l=[]
    for i in range(len(a)):
        l.append( "*" * a[i])
    print(*l, sep='\n')

l=list(map(int,input().split()))
histogram(l)