import random

class Phrases:

    def phrases():
        
        #Creating a list with phrases
        phrases = []
        with open('Hangman\data\phrases.txt', 'r') as ph:
            for line in ph:
                phrases.append(line)

        phrase = random.choice(phrases)
        phrase = phrase.lower()
        phrase = phrase.replace(phrase[-1], '')

        return phrase