import inflect
import sys

p = inflect.engine()

def main():
    name_list = []
    while True:
        try:
            name = input()
            if not name:
                break
            name_list.append(name)
        except EOFError:
           #print()
            break

    print("Adieu, adieu, to " + p.join((name_list)))

main()



