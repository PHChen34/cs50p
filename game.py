import random

def main():

    while True:
        level = input("Level: ")
        try:
            level = int(level)
            break
        except ValueError:
            pass

    ans = random.randint(1, level)
    getans(ans)


def getans(ans):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                pass
            else:
                if guess < ans :
                    print("Too small!")
                elif guess > ans:
                    print("Too large!")
                else:
                    print("Just right!")
                    return 0
        except ValueError:
            pass


if __name__ == "__main__":
    main()
