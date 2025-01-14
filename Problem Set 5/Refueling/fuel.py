def main():
    i = str(input('Fraction: '))
    try:
        percentage = convert(i)
        result = gauge(percentage)
        print(result)
    except (ZeroDivisionError, ValueError) as e:
        print(e)


def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator.")
        percentage = round(x / y * 100)
        return percentage
    except ValueError:
        raise ValueError("Invalid input. Fraction must be in the form 'x/y' with integers.")


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
