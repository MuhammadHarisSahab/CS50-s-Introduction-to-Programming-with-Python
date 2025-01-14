file = str(input("Enter file name: "))
if '.' in file:
    file = file.lower().strip().rsplit('.',1)[1]
else:
    file = file
if file == 'gif':
    print('image/gif')
elif file == 'jpeg' or file =='jpg':
    print('image/jpeg')
elif file == 'png':
    print('image/png')
elif file == 'pdf':
    print('application/pdf')    
elif file == 'zip':
    print('application/zip')
elif file == 'txt':
    print('text/plain')
else:
    print('application/octet-stream')