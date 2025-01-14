def main():
    plate = input('Plate: ')
    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')


def is_valid(s):

    if len(s) >= 2 and s[0].isalpha() and s[1].isalpha():
        pass
    else:
        return False

    if 2 <= len(s) <= 6:
        pass
    else:
        return False

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in s:
        if i not in letters and i not in numbers:
            return False
        else:
            pass
    

    number_started = False
    for char in s:  # Loop through each character
        if char in numbers:  # If the character is a number
            if not number_started:  # If this is the first number
                if char == '0':  # Check if the first number is '0'
                    return False  # Invalid if the first number is '0'
            number_started = True  # Mark that numbers have started
        elif char in letters and number_started:
            return False  # Invalid if a letter appears after numbers
        else:
            pass
    
    return True


if __name__ == "__main__":
    main()
