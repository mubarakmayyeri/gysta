import json
import nltk
from nltk.stem import WordNetLemmatizer




lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())


words = []
classes = []
documents = []
ignore_letters = ['?', '.', ',', '!']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.append(word_list)
        documents.append((word_list, intent['tag']))

        if intent['tag'] not in classes:
            classes.append(intent['tag'])

print(documents)