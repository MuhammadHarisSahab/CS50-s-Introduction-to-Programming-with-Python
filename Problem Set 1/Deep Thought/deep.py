question = str(input("What is the Answer to the Great Question of Life, the Universe and Everything? "))
if question.strip(' ') == '42' or question.lower() == 'forty two' or question.lower() == 'forty-two':
    print('Yes')
else:
    print('No')