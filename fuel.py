while True:
    try:
        frac = input("Fraction: ")
        x, y = frac.split("/")
        x = int(x)
        y = int(y)

        if x > y:
            raise ValueError
        if x < 0:
            raise ValueError

        percent = round((x / y) * 100)
        break

    except (ValueError, ZeroDivisionError):
        pass

if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(f"{percent}%")
