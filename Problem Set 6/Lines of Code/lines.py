import sys
from csv import DictReader

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

file_name = sys.argv[1]
if file_name.split('.')[1] != 'py':
    sys.exit('Not a Python file')

try:
    count = 0
    with open(file_name) as file:
        eader = file.readlines()
        for i in eader:
            x = str(i)
            x = x.lstrip()
            if len(x) != 0:
                if not x.startswith('#'):
                    count += 1
        print(count)
except FileNotFoundError:
    sys.exit('File does not exist')