from validator_collection import validators

email = input('Enter your Email Address: ')

try:
    if x := validators.email(email):
        print('Valid')
except(validators.errors.InvalidEmailError):
    print('Invalid')
