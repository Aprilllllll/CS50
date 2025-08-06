import sys
from pyfiglet import Figlet
figlet = Figlet()

#print(figlet.getFonts())
def selected_font(s, user_arg):
    if user_arg in figlet.getFonts():
        figlet.setFont(font=user_arg)
        return figlet.renderText(s)
    else:
        sys.exit("font does not exist")

if __name__ == "__main__":
    selected_font(s, user_arg)

