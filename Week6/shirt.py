import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command_line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command_line arguments")

input = sys.argv[1]
output = sys.argv[2]
s = (".jpg", ".jpeg", ".png")
if (
    not input.endswith(s)
    or not output.endswith(s)
    or input.split(".")[1] != output.split(".")[1]
):
    sys.exit("Invalid input")

shirt = Image.open("shirt.png")
try:
    with Image.open(input) as image:
        image = ImageOps.fit(image, shirt.size)
        image.paste(shirt, shirt)
        image.save(output)

except FileNotFoundError:
    sys.exit("File does not exist")
