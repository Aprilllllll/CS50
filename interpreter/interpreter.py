import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
}

#ask fomula
express_string=input("Expression: ")

#split string
fomula_set=express_string.split(" ")

#calculator function
def calculator(x, y, z):
    return str(ops[y](x,z))

#run function
#define value
x1=int(fomula_set[0])
z1=int(fomula_set[-1])
y1=fomula_set[1]

result=calculator(x1, y1, z1)
print(result)



