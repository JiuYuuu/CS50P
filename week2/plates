def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not s.isalnum():
        return False

    first_digit_index = -1

    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            first_digit_index = i

            break

    if first_digit_index != -1 and not s[first_digit_index:].isdigit():
        return False

    return True

main()
