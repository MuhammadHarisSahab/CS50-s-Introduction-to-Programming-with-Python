import random

def main():
    level = get_level()
    score = generate_integer(level)
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in [1, 2, 3]:
                return lvl
        except ValueError:
            pass

def generate_integer(level):
    count = 0
    score = 0

    while count < 10:  # Generate 10 problems
        wrong_attempts = 0
        
        # Generate numbers based on the level
        if level == 1:
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
        elif level == 2:
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
        elif level == 3:
            num1 = random.randint(100, 999)
            num2 = random.randint(100, 999)

        answer = num1 + num2
        while wrong_attempts < 3:
            try:
                user_answer = int(input(f"{num1} + {num2} = "))
                if user_answer == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    wrong_attempts += 1
            except ValueError:
                print("EEE")
                wrong_attempts += 1

        if wrong_attempts == 3:
            print(f"{num1} + {num2} = {answer}")

        count += 1  # Count the problem

    return score

if __name__ == "__main__":
    main()
