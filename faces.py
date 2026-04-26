def main():
    s = str (input())
    changed_s = convert(s)
    print(changed_s)

def convert(n):
    n = n.replace(':)', '🙂')
    n = n.replace(':(', '🙁')
    return n

main()
