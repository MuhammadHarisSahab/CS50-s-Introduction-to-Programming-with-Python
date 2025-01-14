import inflect # type: ignore
p = inflect.engine()
a = 'Adieu, adieu, to '
x = []
try:
    while True:
        name = str(input('Name: '))
        x.append(name)
except EOFError:
    False
y = p.join(x)
z = f'{a}{y}'
print(z)