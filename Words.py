import random

class Words:

    def words():
        words = []

        with open('./data/words.txt', 'r', encoding='utf-8') as wr:
            for line in wr:
                words.append(line)

        word = random.choice(words)
        word = word.replace(word[-1], '')
        
        key = []
        for word in word:
            key.append(word)

        answer = key
        
        
        sw2 = True
        while sw2:
            pass
    def selection():
        pass
