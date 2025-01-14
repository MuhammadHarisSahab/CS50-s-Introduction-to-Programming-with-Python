input = str(input('Enter your name: '))
for i in input:
    if i.isupper():
        p = i.lower()
        i = '_' + p
    print(i, end='')