input = str(input('Enter you text: '))
vowels = ['a', 'e', 'i', 'o' ,'u']
for i in input:
    for vowel in vowels:
        if i.lower() == vowel:
            i = ''
    print(i, end = '')