c = input("camelCase: ")
s = ""
for i in range(len(c)):
    if c[i].islower():
        s += c[i]
    elif c[i].isupper():
        s += "_" + c[i].lower()
print(f"snake_case: {s}")
