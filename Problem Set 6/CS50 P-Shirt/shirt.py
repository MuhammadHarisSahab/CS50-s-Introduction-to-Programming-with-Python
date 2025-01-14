from PIL import Image, ImageOps
import sys

if len(sys.argv) > 3:
    sys.exit('Too many command-line arguments')
elif len(sys.argv) < 3:
    sys.exit('Too few command-line arguments')

for x in range(1, 3):
    file, ext = sys.argv[x].split('.')
    if ext.lower() != 'jpg' and ext.lower() != 'jpeg' and ext.lower() != 'png':
        sys.exit('Invalid output')

file1, ext1 = sys.argv[1].split('.')
file2, ext2 = sys.argv[2].split('.')
if ext1 != ext2:
    sys.exit('Input and output have different extensions')

try:
    before = Image.open(f'{sys.argv[1]}')
    shirt = Image.open('shirt.png')
except FileNotFoundError:
    sys.exit('Input does not exist')

before = ImageOps.fit(before, shirt.size)

before.paste(shirt, (0, 0), shirt)

before.save(sys.argv[2])