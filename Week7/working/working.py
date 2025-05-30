import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    match = re.search(
        r"^(\d{1,2}):?(\d{2})?\s(AM|PM)\sto\s(\d{1,2}):?(\d{2})?\s(AM|PM)$",s
    )
    if not match:
        raise ValueError("Invalid format")

    h1, m1, ap1, h2, m2, ap2 = match.groups()

    if m1 is None or m2 is None:
        m1, m2 = 0, 0
    h1, m1, h2, m2 = map(int, [h1, m1, h2, m2])

    if ap1 == "PM" and h1 != 12:
        h1 += 12
    elif ap1 == "AM" and h1 == 12:
        h1 = 0

    if ap2 == "PM" and h2 != 12:
        h2 += 12
    elif ap2 == "AM" and h2 == 12:
        h2 = 0

    if (
       not 0 <= h1 <= 23
        or not 0 <= h2 <= 23
        or not 0 <= m1 <= 59
        or not 0 <= m2 <= 59
    ):
        raise  ValueError("Invalid time value")

    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


if __name__ == "__main__":
    main()
