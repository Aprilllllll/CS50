import random

def game_module():
    while True:
        i = input("Level: ")
        try:
            _i = int(i)
            a = random.randint(1, _i)
            while True:
                try:
                    g = int(input("Guess: "))
                    if g <= 0:
                        continue
                    elif a == g:
                        print("Just right! ")
                        return
                    elif a > g:
                        print("Too small! ")
                        continue
                    elif a < g:
                        print("Too large! ")
                        continue
                except ValueError:
                    continue
        except ValueError:
            continue
        except EOFError:
            break

game_module()

