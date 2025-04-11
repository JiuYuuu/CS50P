import inflect

names = []
p = inflect.engine()
while True:
    try:
        names.append((input("Name: ")).strip())
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {p.join(names)}")
