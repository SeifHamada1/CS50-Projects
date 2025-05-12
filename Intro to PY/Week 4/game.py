import random
while True:
    try:
        level = int(input("Level: "))
        answer = random.randint(1,level)
        while True:
            guess = int(input("Guess: "))
            if guess > 0:
                pass
            if answer > guess:
                print("Too small!")
            elif answer < guess:
                print("Too large!")
            else:
                print("just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break
