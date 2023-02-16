class Account():
    def __init__(self,owner,balance) :
        self.owner=owner
        self.balance=balance
    def dep(self,dep):
        self.dep=dep
        self.balance+=dep
    def withdraw(self,withdraw):
        self.withdraw=withdraw
        if self.balance>=self.withdraw:
            self.balance-=self.withdraw
        else:
            print("no")
    def show(self):
        print("owner ",self.owner," has ",self.balance)
a=str(input())
b=int(input())
ans=Account(a,b)
ans.show()

dep=int(input())
ans.dep(dep)
ans.show()

wi=int(input())
ans.withdraw(wi)
ans.show()