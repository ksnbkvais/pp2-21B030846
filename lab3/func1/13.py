import random
n=random.randint(1,20) 
i=1
def numb(a,i):
    
    if a==n:
        print ("Good job," , name, "! You guessed my number in ",i," guesses!")
    else:
        if a<n:
            print("Your guess is too low.")
            
        else:
            print("Your guess is too high.")
        print("Take a guess.")
        
        numb(int(input()),i+1)

print("Hello! What is your name?")
name=str(input())
print("Well, ", name , ", I am thinking of a number between 1 and 20.")
print("Take a guess.")
a=int(input())
numb(a,i)


