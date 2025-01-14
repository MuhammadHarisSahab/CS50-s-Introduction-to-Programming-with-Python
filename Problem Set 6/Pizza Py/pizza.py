import sys
from tabulate import tabulate 
import csv

if len(sys.argv) > 2:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 2:
    sys.exit('Too few command-line arguments')

file_name = sys.argv[1]
if file_name.split('.')[1] != 'csv':
    sys.exit('Not a CSV file')

menu = []

try:
    with open(file_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            menu.append(row)
        h1, h2, h3 = row
        print(tabulate(menu, headers = 'keys', tablefmt = "grid"))
except(FileNotFoundError):
    sys.exit('File does not exist')