import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    if match := re.search('.+(https?://(:?www\.)?youtube\.com/embed/.+)".+$', s):
        x = match[1].replace('embed/', '')
        if 'youtube.com' in x:
            x = x.replace('youtube.com', 'youtu.be')
        if 'http://' in x:
            x = x.replace('http://', 'https://')
        if 'www.' in x:
            x = x.replace('www.','')
        return x



if __name__ == "__main__":
    main()