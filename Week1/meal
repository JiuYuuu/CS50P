def main():
    time = convert(input("What's time is it?").strip())
    if 7 <= time <= 8:
        print("Breakfast time")
    if 12 <= time <= 13:
        print("Lunch time")
    if 18 <= time <= 19:
        print("Dinner time")

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

if __name__ == "__main__":
    main()
