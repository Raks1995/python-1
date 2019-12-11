secret = 17

guess = int(input("Which number between 0 to 20 did I imagine?: "))

if guess == secret:
    print("Yes")
else:
    print("No, the number is not " + str(guess))
