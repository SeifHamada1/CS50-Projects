def main():
    i = input("")
    print(convert(i))


def convert(i):
    if ":)" in i or ":(" in i:
        c = i.replace(":)", "🙂")
        return c.replace(":(", "🙁")


main()
