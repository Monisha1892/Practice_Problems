print("""Welcome to Guessing Game. 
You will get three chances to win.
Please enter a number between 1 to 9 at each chance.
If the number matches the lucky number you win today
""")
i = 1
while i <= 3:
    guess = int(input("guess: "))
    i += 1
    if guess == 2:
        print("you win")
        break
else:
        print("Sorry you failed")
print("""Done.
Thanks for playing the game.""")
