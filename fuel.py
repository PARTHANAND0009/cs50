while True:
    a = input("Fraction: ")
    x, y = a.split("/")
    x = int(x)
    y = int(y)
    if y == 0:
        print("Error: Denominator cannot be zero.")
    elif x < y:
        print(f"{(x / y) * 100:.0f}%")
        break
    elif x == y:
        print("F")
    else:
        pass
