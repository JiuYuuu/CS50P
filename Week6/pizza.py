import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
filename = sys.argv[1]
if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(filename) as filename:
        reader = csv.DictReader(filename)
        data = list(reader)
        print(tabulate(data, headers="keys", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exist")
