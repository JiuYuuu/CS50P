def main():
    greeting = input("Greeting: ").strip().lower()
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0

    elif greeting == ("what's happening?") or greeting == ("what's up?"):
        return 100

    else:
        return 20

if __name__ == "__main__":
    main()
