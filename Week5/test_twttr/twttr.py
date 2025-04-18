def main():
    s = input("Input: ")
    print("Output: ", shorten(s))

def shorten(s):
    ans = "".join([c for c in s if c.lower() not in "aeiou"])
    return ans

if __name__ == "__main__":
    main()
