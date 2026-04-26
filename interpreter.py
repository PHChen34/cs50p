def main():
    x, y, z = input("Expression: ").split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        print(f"{plus(x, z):.1f}")
    if y == "-":
        print(f"{minus(x, z):.1f}")
    if y == "/":
        print(f"{divide(x, z):.1f}")
    if y == "*":
        ans4 = float()
        print(f"{times(x, z):.1f}")


def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def divide(a, b):
    return a / b

def times(a, b):
    return a * b

main()
