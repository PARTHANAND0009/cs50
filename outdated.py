month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        a = input("Date: ")
        m, d, y = a.split("/")
        m = int(m)
        d = int(d)
        y = int(y)
        if m < 1 or m > 12 or d < 1 or d > 31 or y < 0:
            pass
   
        print(f"{y}-{m:02}-{d:02}")
        break
    except ValueError:
        pass