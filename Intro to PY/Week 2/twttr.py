input = input("Input: ")
output = ""
for letters in range(len(input)):
    if input[letters].lower() not in ["a","e","i","o","u"]:
        output = output + input[letters]
print(f"output: {output}")
