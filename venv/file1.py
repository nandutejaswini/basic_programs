hidden = 4
guess = int(input("guess the number : "))
print(guess)
while guess != hidden :
    print(guess, "not correct")
    guess=int(input("try another : "))
print(guess, "was correct")