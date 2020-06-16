puntajes = [{'letters':'AEIOULNRST', 'score': 1},
{'letters':'DG', 'score': 2},
{'letters':'BCMP', 'score': 3},
{'letters':'FHVWY', 'score': 4},
{'letters':'K', 'score': 5},
{'letters':'JX', 'score': 8},
{'letters':'QZ', 'score': 10}]

def get_score(value):
    for i, dic in enumerate(puntajes):
        if value in dic['letters']:
            return dic['score']
            #return i
    return 0

def scrabble_score(word):
    word = str(word).upper()
    score = 0
    for c in word:
        score = score + get_score(c)
    return score


