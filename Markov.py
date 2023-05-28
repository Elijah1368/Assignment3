import random
import string
import os
from collections import defaultdict

# Path to the text files
#file_paths = ['stud.txt', 'sign.txt']
file_paths = ['example.txt']

def preprocess(file_paths):
    model = defaultdict(lambda: defaultdict(list))

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read().lower()
            words = text.translate(str.maketrans('', '', string.punctuation)).split()

            for i in range(2, len(words)):
                seq = ' '.join(words[i-2:i])
                model[seq][words[i]].append(words[i])
    return model

def generate_sentence(model):
    seq = random.choice(list(model.keys()))
    story = seq.split()

    while len(story) < 2000:
        if model[seq]:
            possibilities = list(model[seq].keys())
            next_word = random.choices(possibilities, weights=[len(model[seq][p]) for p in possibilities], k=1)[0]
            story.append(next_word)
            seq = ' '.join(story[-2:])
        else:
            seq = random.choice(list(model.keys()))
    return ' '.join(story)

def write_story(story):
    with open('Readme.txt', 'w', encoding='utf-8') as file:
        file.write(story)

# Build the model
model = preprocess(file_paths)

for key, value in model.items():
    print(key, ':', value)
# Generate the story
#story = generate_sentence(model)

# Write the story to a file
#write_story(story)
