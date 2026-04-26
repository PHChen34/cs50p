import sys

def main():
    check()
    counter = 0
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if not line.isspace() and not line.lstrip().startswith("#"):
                    counter += 1
        print(counter)
    except FileNotFoundError:
        sys.exit("File does not exist")


def check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" not in sys.argv[1]:
        sys.exit("Not a python file")


def checkline(line):
    if line.isspace():
        return True
    if line.strip().lstrip().startswith('#'):
        return True

    return False



if __name__ == "__main__":
    main()
