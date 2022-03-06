import random

def words():
    words = []

    with open('./data/words.txt', 'r', encoding='utf-8') as wr:
        for line in wr:
            words.append(line)

    word = random.choice(words)
    word = word.replace(word[-1], '')
    
    answer = []
    for word in word:
        answer.append(word)

    sw2 = True

    while sw2:
        pass

