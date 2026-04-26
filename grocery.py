dic = {}

while True:
    try:
        item = input().upper()
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1

    except EOFError:
        for items in sorted(dic):
            print(dic[items], items)
        break





