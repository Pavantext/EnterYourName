import pyfiglet
from termcolor import colored

# Create a PyFiglet font object
font = pyfiglet.Figlet()

# Your text to be displayed
text = input("Enter Your Name:-\n")
color = input("Enter color you want:-\n\n(ex:-black','grey','red'\n'green','yellow','blue'\n'magenta','light_grey'\n'dark_grey','light_red','light_green'\n'light_yellow','light_blue','light_magenta'\n'light_cyan','white')\n")

ascii_art = font.renderText(text)

# Print colored ASCII art
colored_ascii_art = colored(ascii_art, color, "on_black",['bold'])
print(colored_ascii_art)
