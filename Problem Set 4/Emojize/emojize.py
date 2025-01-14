import emoji

# Input from user
q = input('Input: ')  # Use input without casting to str (not necessary)

# Process and print the emojized string
print(emoji.emojize(q, language= 'alias'))
