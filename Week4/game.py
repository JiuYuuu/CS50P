import random

while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        pass

ans = random.randint(1, n)
while True:
    try:
        guess = int(input("Guess: "))
        if guess < ans:
            print("Too small!")
        elif guess > ans:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
