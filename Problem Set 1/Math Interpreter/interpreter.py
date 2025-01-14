def calc():
    q = input('Enter your calculation: ')
    q = q.lower().strip().split(' ')
    x = int(q[0])
    y = q[1]
    z = int(q[2])
    if y == '+':
        print(float(x+z))
    elif y == '-':
        print(float(x-z))
    elif y == '/':
        print(float(x/z))
    elif y == '*':
        print(float(x*z))
calc()