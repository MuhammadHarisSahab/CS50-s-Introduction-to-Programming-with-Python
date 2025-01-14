import sys
from csv import DictReader, DictWriter

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')



with open(sys.argv[1], 'r') as read, open(sys.argv[2], 'w') as write:
    reader = DictReader(read)
    writer = DictWriter(write, fieldnames = ['first', 'last', 'house'])
    writer.writeheader()
    for rows in reader:
        last, first = rows['name'].split(',')
        writer.writerow({
            'first' : first.strip(),
            'last' : last,
            'house' : rows['house']
        })
        


