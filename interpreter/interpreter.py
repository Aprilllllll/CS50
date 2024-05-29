#ask fomula
express_string=input("Expression: ")

#split string
fomula_set=express_string.split(" ")

#calculator function
def symbol_converter(s)
    match s:
        case "/":
            return '/'



#convert
x1=int(fomula_set[1])
z1=fomula_set[-1]
y1=int(fomula_set[-2])

