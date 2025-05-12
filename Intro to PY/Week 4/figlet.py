import sys
import pyfiglet
fonts = ['alphabet', 'slant', 'rectangles', 'regular']
if len(sys.argv) == 1:
    figlet = pyfiglet.Figlet()
elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in fonts:
            x = input("Input: ")
            figlet = pyfiglet.Figlet(sys.argv[2])
else:
    sys.exit("Invalid usage")
print(figlet.renderText(x))
