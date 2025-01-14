def main():
    p = check()
    while p == None:
        p = check()
    p = int(p)
    p = str(p) + '%'
    if p == '100%' or p == '99%':
        p = 'F'
    elif p == '0%' or p == '1%':
        p = 'E'
    print(p)

def check():
    while True:
        try:
            q = input('Fraction: ')
            q = q.split('/')
            x = int(q[0])
            y = int(q[1])
            if x > y:
                break
            p = float(round(((x/y) * 100)))
            return p
        except(ValueError, ZeroDivisionError):
            pass


main()