months = [
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
    date = input("Date: ")
    if len(date.split("/")) == 3:
        date = date.split("/")
        try:
            m, d, y = map(int, date)
            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y}-{m:02d}-{d:02d}")
                break
        except ValueError:
            pass

    else:
        mon = date.split(" ")
        if len(mon) == 3:
            m, d, y = date.split(" ")
            try:
                if "," in d:
                    d = d.replace(",", "")
                    d, y = int(d), int(y)
                    if m in months:
                        m = months.index(m) + 1
                        if 1 <= m <= 12 and 1 <= d <= 31:
                            print(f"{y:04d}-{m:02d}-{d:02d}")
                            break

            except ValueError:
                pass
