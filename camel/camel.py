def main(camelCase):
    str_camelCase=str(camelCase)
    for a in str_camelCase:
        if 'a' <= a <= 'z':
            print(a,end="")
        else:
            print("_"+a.lower() ,end="")


camelCase = input("camelCase: ")

print("snake_name: ", end="")
str(main(camelCase))


