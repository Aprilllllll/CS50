import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

#ask fomula
express_string=input("Expression: ")

#split string
fomula_set=express_string.split(" ")

#define value
x1=int(fomula_set[1])
z1=fomula_set[-1]
y1=int(fomula_set[-2])

#calculator function
def calculator(x, y, z):
    return ops[y](x,z)

#run function

calculator(x1, y1, z1)


