import random
num=random.randint(1,100)
i = None
guess=0
while(i!=num):
    i=int(input("Enter a number from 1 to 100\t"))
    guess+=1
    if(i==num):
        print("Your guess is right")
    elif i<num:
        print("Greater number PLEASE")
    elif i>num:
        print("Smaller number PLEASE")
print(f"You guessed it in {guess} guesses")

with open("highscore.txt","rt") as f:
    high=int(f.read())
if guess<high:
    with open("highscore.txt","wt") as f:    
        f.write(str(guess))
    
    