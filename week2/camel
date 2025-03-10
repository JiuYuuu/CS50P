def main():
    camel = input("camelCase: ").strip()
    print("snake_case: ", end="")
    translate(camel)

def translate(name):
    for c in name:
        if c.isupper():
            print("_" + c.lower(), end="")
        else:
            print(c, end="")
    print()
if __name__ == '__main__':
    main()
