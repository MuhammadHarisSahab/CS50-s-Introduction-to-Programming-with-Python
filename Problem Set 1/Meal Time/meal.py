def main():
    q = input("What time is it? ")
    time = convert(q)
    if 7 <= time <= 8:
        print('breakfast time')
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):

    if ':' in time:
        time = time.split(":")
        hrs = float(time[0])
        mins = float(time[1])
        if 0 <= mins <= 60:
            mins = mins/60
            hrs += mins
            return float(hrs)
            


if __name__ == "__main__":
    main()