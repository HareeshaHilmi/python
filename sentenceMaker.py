def sentenceMaker(sentence):
    questionWords = ("what", "how", "why")

    capitaized = sentence.capitalize()
    if sentence.startswith(questionWords):
        return "{}?".format(capitaized)
    else:
        return "{}".format(capitaized)

result = []

while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        result.append(sentenceMaker(user_input))

print(" ".join(result))