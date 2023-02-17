def prime(x):
    k=1
    for i in range(2,x):
            if x%i==0:
                k=0
                break
            else:
                k=1
    return k
    


my_list=list(map(int, input().split()))
result = list(filter(lambda x: (prime(x)), my_list))
print(result)