from pyfiglet import Figlet
figlet = Figlet()
import sys
import random

commands = ["-f", "--fonts"]
fonts = figlet.getFonts()



if len(sys.argv) == 1:
    newfonts = random.choice(fonts)


if sys.argv[1] in commands and sys.argv[2] in fonts and len(sys.argv) == 3:
    newfonts = sys.argv[2]
else:
    sys.exit("Invalid usage")

string = input("Input: ")
figlet.setFont(font = newfonts)
print(figlet.renderText(string))


