d = {}

while True:
    try:
        item = input("Item: ").upper()
        if item in d:
            d[item] = d[item] + 1
        else:
            d[item] = 1
    except EOFError:
        for a in sorted(d):
            print(d[a],a)
        break