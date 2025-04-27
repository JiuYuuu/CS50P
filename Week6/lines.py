import sys

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
filename = sys.argv[1]
if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(filename) as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

count = 0
for line in lines:
    l = line.strip()
    if l == "" or l.startswith("#"):
        continue
    count += 1

print(count)
