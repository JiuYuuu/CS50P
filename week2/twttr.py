s = input("Input: ").strip()

ans = "".join ([c for c in s if c.lower() not in "aeiou"])

print("Output:", ans)
