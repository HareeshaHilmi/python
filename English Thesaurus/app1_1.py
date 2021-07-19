import json
from difflib import get_close_matches
from os import path

data = json.load(open("E:\\Practice\\udemy\\Python\\App\\English Thesaurus\\data.json"))


def dictionary(word):

    word = word.lower()
    if word in data:    # exist word
        return data[word]
    elif word.title() in data:  #Start with capita
        return data[word.title()]
    elif len(get_close_matches(word, data.keys())) > 0: #User mistakes
        yn = input("Did you mean %s instead? Enter Y if yes, or N if not :  " % get_close_matches(word, data.keys())[0])
        if yn == "Y":   #User select correct word
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":     # not user defined
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please check again."

word = input("Enter a word: ")

output = dictionary(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)