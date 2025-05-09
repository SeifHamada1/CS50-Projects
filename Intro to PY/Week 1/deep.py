answer = input("What is the answer to the Great Question of Life, the Universe and Everything").lower().strip()

if answer == str(42):
    print("Yes")
elif answer =="forty two":
    print("Yes")
elif answer =="forty-two":
    print("Yes")
else:
    print("No")
