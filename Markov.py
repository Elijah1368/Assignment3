'''
Creates a Tri-Gram Markov Model based on two ofthe chosen Sherlack Holmes' stories.
'''
import random
from collections import defaultdict

class Markov:
    def __init__(self):
        # Initialize the model as a nested defaultdict.
        # The outer defaultdict maps a two-word sequence to another defaultdict.
        # The inner defaultdict maps a following word to its frequency.
        self.model = defaultdict(lambda: defaultdict(int))

    def preprocess(self, words):
        """Builds a Markov model based on a list of words."""
        for i in range(2, len(words)):
            # Get a sequence of two words
            seq = ' '.join(words[i-2:i])
            # Increment the frequency of the word following the sequence
            self.model[seq][words[i]] = self.model[seq][words[i]] + 1

    def generate_story(self):
        """
        Generates a story of 2000 words using the Markov model.
        
        The story starts with a randomly chosen two-word sequence from the model.
        Then, it uses the model to generate each subsequent word based on the
        frequency of that word following the current two-word sequence.
        
        If the model contains no information about the current sequence, it
        chooses another random sequence from the model and continues from there.
        
        Returns the story as a string.
        """
        # Start with a random two-word sequence from the model
        seq = random.choice(list(self.model.keys()))
        # Split the sequence into a list of words
        story = seq.split()

        # Continue generating words until the story is 2000 words long
        while len(story) < 2000:
            if self.model[seq]:
                # Get the possible words that could follow the current sequence
                possibilities = list(self.model[seq].keys())
                # Get the frequencies of these words
                weights = [self.model[seq][p] for p in possibilities]
                # Choose a word based on its frequency
                next_word = random.choices(possibilities, weights, k=1)[0]
                # Add the chosen word to the story
                story.append(next_word)
                # Update the sequence to be the last two words
                seq = ' '.join(story[-2:])
            else:
                # If there's no data for the current sequence, choose a new sequence
                seq = random.choice(list(self.model.keys()))
        # Join the story list back into a string and return it
        return ' '.join(story)
