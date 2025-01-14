import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    
    if match := re.search( r'^(?P<hr1>([0-9]{1,2}:[0-9]{1,2})?([0-9]{1,2})?\s(AM|PM))\sto\s(?P<hr2>([0-9]{1,2}:[0-9]{1,2})?([0-9]{1,2})?\s(AM|PM))$', s):
        a, b = match.group('hr1'), match.group('hr2')

        if ':' in a:
            time1 = divide(a)
        else:
            time1 = dividde(a)
        if ':' in b:
            time2 = divide(b)
        else:
            time2 = dividde(b)
        
        
        time = f'{time1} to {time2}'
        
        return time
    else:
        raise ValueError

def divide(x):
    a, b = x.split(' ')
    hr, min = a.split(':')
    hr = int(hr)
    min = int(min)

    if 12 < hr < 0 or min > 59:
        raise ValueError
    if b == 'PM':
        hr += 12
    if hr == 12:
        hr = 0
    if hr == 24:
        hr = 12

    time = f'{hr:02}:{min:02}'
    return time

def dividde(y):
    
    hr, b = y.split()
    min =    0
    hr = int(hr)

    if 12 < hr < 0 or min > 59:
        raise ValueError
    if b == 'PM':
        hr += 12
    if hr == 12:
        hr = 0
    if hr == 24:
        hr = 12

    time = f'{hr:02}:{min:02}'
    return time



if __name__ == "__main__":
    main()