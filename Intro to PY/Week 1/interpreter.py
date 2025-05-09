x, y, z = input("Expression: ").split(" ")

match y:
    case "+":
        print(float(x) + float(z))

match y:
    case "-":
        print(float(x) - float(z))

match y:
    case "*":
        print(float(x) * float(z))

match y:
    case "/":
        print(float(x) / float(z))
