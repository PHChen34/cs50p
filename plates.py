def main():
    plate = input("Plate: ")

    for cha in plate:
        if not cha.isalpha() and not cha.isdigit():
            print("Invalid")
            return 0

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # 1. 長度
    if not (2 <= len(s) <= 6):
        return False

    # 2. 前兩個字母
    if not s[0:2].isalpha():
        return False

    number_started = False

    for c in s:
        if c.isdigit():
            if not number_started:
                if c == "0":
                    return False
                number_started = True
        else:  # 是字母
            if number_started:
                return False

    return True


main()

