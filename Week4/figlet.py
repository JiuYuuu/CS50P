import sys
import random
from pyfiglet import Figlet

fonts = Figlet().getFonts()
if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit("Invalid argument")
else:
    sys.exit("Invalid argument")

t = input("Input: ")
print("Output: \n", Figlet(font=font).renderText(t))
