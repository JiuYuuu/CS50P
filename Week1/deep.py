user_input = input("What is the Answer yo the Great Question of Life, the Universe, and Everything?").strip().lower()

match user_input:
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case _:
        print("No")
