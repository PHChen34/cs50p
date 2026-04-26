import random


def main():
    l = get_level()
    x, y = generate_integer(l)
    score = 0

    #start asking question
    for i in range(10):
        #print quesion
        correct = int(x[i]) + int(y[i])
        for j in range(3):
            #check answer
            if j == 2:
                ans = int(input(f"{x[i]} + {y[i]} = "))
                if ans == correct:
                    score += 1
                    break
                else:
                    print("EEE")
                    print(f"{x[i]} + {y[i]} = {correct}")
                    break               #break 檢查的小迴圈

            try:
                ans = input(f"{x[i]} + {y[i]} = ")
                ans = int(ans)
                if ans == correct:
                    score += 1
                    break
                else:
                    print("EEE")
                    pass

            except ValueError:
                print("EEE")
                pass


    print(f"score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level==1 or level == 2 or level == 3:
                return level
            else:
                pass
        except ValueError:
            pass

def generate_integer(l):
    digitx = []
    digity = []
    if l == 1:
        for i in range(10):
            numx = random.randint(0,9)
            digitx.append(numx)
            numy = random.randint(0,9)
            digity.append(numy)
        return digitx, digity

    if l == 2:
        for i in range(10):
            numx = random.randint(10,99)
            digitx.append(numx)
            numy = random.randint(10,99)
            digity.append(numy)
        return digitx, digity

    if l == 3:
        for i in range(10):
            numx = random.randint(100,999)
            digitx.append(numx)
            numy = random.randint(100,999)
            digity.append(numy)
        return digitx, digity


if __name__ == "__main__":
    main()
