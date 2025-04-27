def main():
    while True:
        try:
            frac = input("Fraction: ")
            percent = convert(frac)
            print(gauge(percent))
            break
        except(ValueError, ZeroDivisionError)
            pass

def convert(fraction):
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)
    if  y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    if 0 <= x / y <= 1:
        return round(x / y * 100)
    break

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
