greet = input("Greeting: ").strip().lower()

if greet == "hello" or greet.startswith("hello"):
    print("$0")
elif greet[0] == "h":
    print("$20")
else:
    print("$100")
