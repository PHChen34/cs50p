def main():
    amountdue = 50

    while amountdue > 0:
        print(f"Amount due: {amountdue}")
        coin = getcoin()

        if coin in [25, 10, 5]:
            amountdue = amountdue - coin

    print(f"Change Owed: {-amountdue}")




def getcoin():
    while True:
        try:
            return int(input("Insert coin: "))
        except ValueError:
            pass


main()
