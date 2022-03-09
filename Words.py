import random

class Words:

    def words():

        #Creating a list with words
        words = []
        with open('Hangman\data\words.txt', 'r', encoding='utf-8') as wr:
            for line in wr:
                words.append(line)

        #Pick a random word of the list
        word = random.choice(words)
        word = word.replace(word[-1], '')

        return word