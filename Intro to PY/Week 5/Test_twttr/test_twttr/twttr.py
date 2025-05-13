def main():
    string = input("Input: ")
    print(shorten(string))

def shorten(text):
    output = ""
    for letters in range(len(text)):
        if text[letters].lower() not in ["a","e","i","o","u"]:
            output = output + text[letters]
    return f"{output}"
if __name__ == "__main__":
    main()


