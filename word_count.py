import re
def word_count(phrase):
    phrase = str(phrase).lower()
    phrase = re.sub('[^a-zA-Z0-9\' ]', ' ', phrase)
    phrase = " ".join(phrase.split()) 
    words = phrase.split(' ')
    diccionario = []
    for word in words:
        word = clean_word(word)
        encontrado = find(diccionario, 'word', word)
        if(encontrado == -1):
            diccionario.append({'word': word, 'total' : 1})
        else:
            diccionario[encontrado]['total'] = diccionario[encontrado]['total'] + 1
    return diccionario

def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

def clean_word(word):
    if word.startswith("'") or word.endswith("'"):
        if word.startswith("'"):
            word = word[1:]
        if word.endswith("'"):
            word = word[0:len(word) -1]
    return word