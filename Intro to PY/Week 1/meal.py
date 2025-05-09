def main():
    time = input("What time is it? ")
    z = convert(time)
    if z >= 7 and z <= 8:
        print("breakfast time")

    elif z >= 12 and z <= 13:
        print("lunch time")

    elif z >= 18 and z <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    x = float(float(minutes) / 60)
    y = float(hours)
    return x + y

if __name__ == "__main__":
    main()
