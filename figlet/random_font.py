import random
from pyfiglet import Figlet

s = "hello"

def Random_font(s):
    figlet = Figlet()
    fonts = figlet.getFonts()
    r_font_name = random.choice(fonts)
    figlet.setFont(font=r_font_name)
    return figlet.renderText(s)

if __name__ == "__main__":
    print(Random_font(s))

#print(random_font)////for debug



