while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        if x > y:
            raise ValueError
        if 0 <= x / y <= 1:
            percentage = round(x / y * 100)
        break


    except (ValueError, ZeroDivisionError):
        pass

if percentage >= 99:
    print("F")
elif percentage <= 1:
    print("E")
else:
    print(f"{percentage}%")
