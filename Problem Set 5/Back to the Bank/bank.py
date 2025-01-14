def main():
    greetings = input('Greetings: ')  # Take user input
    print(f"${value(greetings)}")  # Pass user input to the value function


def value(greeting):
    
    greeting = greeting.lower()
    # Check for "hello" in the greeting
    greeting = greeting.lower()
    if 'hello' in greeting:
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
