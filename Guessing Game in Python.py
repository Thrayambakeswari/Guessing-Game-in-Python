import random as r #imported the module
num = r.randrange(100)
Guess = 5 #count variable
while Guess >=0:
    your_guess = int(input("Enter your Guess"))
    def check(x):
        if your_guess == x:
            print('you win')
        elif your_guess > x:
            print("You are close, keep trying lower")
        else:
            print("You are close, keep trying higher")
    if Guess > 1:
        check(num)
    elif Guess == 1:
        check(num)
        print("This is your last chance, make the most of it")
    else:
        print("You lost")
    Guess = Guess - 1