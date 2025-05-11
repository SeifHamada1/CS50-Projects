items = []
while True:
    try:
        item = input("")
        items.append(item)
    except EOFError:
        print()
        break
items.sort()
for item in sorted(set(items)):
    print(f"{items.count(item)} {item.upper()}")
