while True:
    try:
        x,y=input("Fraction: ").split("/")
        if(int(x) > int(y)):
            continue
        elif ((int(x) / int(y)) * 100) <= 1:
            print("E")
        elif ((int(x) / int(y)) * 100) >= 99:
            print("F")
        else:
            print(f"{round(((int(x) / int(y)) * 100))}%")
        break
    except (ZeroDivisionError, ValueError):
        pass






