import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command_line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command_line arguments")

students = []
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            name  = row["name"]
            house = row["house"]

            last, first = name.split(", ")
            students.append({"first": first, "last": last, "house": house})

    with open(sys.argv[2], "w", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in students:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
