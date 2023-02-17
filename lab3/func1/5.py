from itertools import permutations
def permutation(s):
    l=[]
    for i in s:
        l.append(i)
    l.sort()
    perm = permutations(l)
    for i in perm:
        print(*i, sep='')
    
s = input()
permutation(s)