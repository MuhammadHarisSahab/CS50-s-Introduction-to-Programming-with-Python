try:
    abc = {}
    while True:
            item = str(input('')).upper()
            if item in abc:
                 abc[item] += 1
            else:
                 abc[item] = 1   
except EOFError:
    False

    for item, count in sorted(abc.items()):
        print(f'{count} {item}')
    

    