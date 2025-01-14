import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$',ip):
        a, b, c, d = match[1], match[2], match[3], match[4]
        a, b, c, d = int(a), int(b), int(c), int(d)
        if 0 <= a < 256 and 0 <= b < 256 and 0 <= c < 256 and 0 <= d < 256:
            return True
        else:
            return False
    return False


if __name__ == "__main__":
    main()