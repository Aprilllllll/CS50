import sys
from random_font import Random_font
from selected_font import selected_font
from pyfiglet import Figlet
figlet = Figlet()

def main():
    if len(sys.argv) == 1:
        s = input("Input: ")
        print("random font")
        print(Random_font(s))
    elif len(sys.argv) < 2:
        sys.exit()
    elif len(sys.argv) > 4:
        sys.exit("too many arguments")
    elif sys.argv[1] == '-f':
        #print("it is -f")
        user_arg = sys.argv[-1]
        if not user_arg in figlet.getFonts():
            sys.exit("Font not exist")
        else:
            s = input("Input: ")
            print(selected_font(s,user_arg))
    elif sys.argv[1] == "--font":
        #print(f"it is --font")
        user_arg = sys.argv[-1]
        if not user_arg in figlet.getFonts():
            sys.exit("Font not exist")
        else:
            s = input("Input: ")
            print(selected_font(s,user_arg))
    else:
        sys.exit("arguement not right")


main()
