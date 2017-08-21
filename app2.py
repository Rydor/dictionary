import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys(), cutoff=0.8)) > 0:
        close = get_close_matches(word, data.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: "
        % close)
        if yn == "Y" or yn == "y":
            return data[close]
        elif yn == "N" or yn == "n":
            return "The word does not exist."
        else:
            return "We didn't understand your entry."
    else:
        return "The word does not exist. Please double check it."



word = input("Enter word: ")
result = translate(word)
if type(result) == list:
    for i in result:
        print(i)
else:
    print(result)
