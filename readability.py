text = input("Text: ")

nletters = 0
for i in range(len(text)):
    if text[i].isalpha():
        nletters += 1

nwords = 1
for i in range(len(text)):
    if text[i].isspace():
        nwords += 1

nsentences = 0
for i in range(len(text)):
    if text[i] == "." or text[i] == "!" or text[i] == "?":
        nsentences += 1


l = (float(nletters) / float(nwords) * 100)
s = (float(nsentences) / float(nwords) * 100)
index = round(0.0588 * l - 0.296 * s - 15.8)


if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")
