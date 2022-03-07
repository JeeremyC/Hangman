from multiprocessing.reduction import duplicate
import random
from turtle import st

class Words:

    def words(diff):


        #Amount of lives
        if diff == 1:
            lives = 10
        elif diff == 2:
            lives = 5
        elif diff == 3:
            lives = 3
        else: 
            pass #Catch an error


        #Creating a list with words
        words = []
        with open('Hangman\data\words.txt', 'r', encoding='utf-8') as wr:
            for line in wr:
                words.append(line)

        #Pick a random word of the list
        word = random.choice(words)
        word = word.replace(word[-1], '')
        
        #Convert that word in an array of characters "key" 
        #key = []
        #for word in word:
        #    key.append(word)

        #Duplicate that and replace each character by underscore
        key = word
        mytable = key.maketrans("qwertyuiopasdfghjklzxcvbnm","__________________________")
        print(key.translate(mytable))
      
    def selection():
        pass
