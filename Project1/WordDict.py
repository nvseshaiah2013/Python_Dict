import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(x):
    if x.lower() in data.keys():
        return data[x]
    elif len(get_close_matches(x,data.keys()))>0:
        best_match = get_close_matches(x,data.keys())[0]
        print('Did you mean %s instead?'% best_match)
        inp = input('Enter Y if yes, N if no:\n')
        if inp == 'Y':
            return data[best_match]
        elif inp == 'N':
            return ["Oops! It seems that the word is incorrect"]
        else:
            return ['Incorrect Option Chosen']
    else:
        return ["Oops! Word not found"]

word = input("Enter a Word to Know meaning:\n")
print(*translate(word),sep='\n')

