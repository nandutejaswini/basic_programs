import random
hidden= random.randint(1,20)
print(hidden)
guess = int(input("guess the number : "))
while guess!= hidden:
    if guess<hidden :
        print(guess, "too less")
    else:
        print(guess,"too high")
    guess=int(input("try another"))
print(guess, "was correct")

