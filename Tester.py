"""
This script generates a story based on a Markov model trained on the text from a list of files.

The script first creates an instance of the Markov model. Then, for each file in the list, it reads the file's text, 
converts it to lowercase, removes punctuation, and splits it into a list of words. It preprocesses these words to build 
the Markov model.

After building the model, the script generates a story using the model and writes the story to an output file.
"""

from Markov import Markov
import string

# Define the paths to the input text files
file_paths = ['stud.txt', 'sign.txt']

if __name__ == '__main__':
    # Instantiate the Markov model
    Model = Markov()
    
    # Loop through each file
    for file_path in file_paths:
        # Open the file and read its content
        with open(file_path, 'r', encoding='utf-8') as file:
            # Convert the text to lowercase
            text = file.read().lower()
            # Remove punctuation from the text and split it into words
            words = text.translate(str.maketrans('', '', string.punctuation)).split()
            # Preprocess the words to build the Markov model
            Model.preprocess(words)
            
    # Generate a story using the Markov model
    story = Model.generate_story()
    
    # Write the generated story to the output file
    with open('Readme.txt', 'w', encoding='utf-8') as file:
        file.write(story)
