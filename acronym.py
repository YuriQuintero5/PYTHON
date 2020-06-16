def acronym(word):
    result = ''
    word = str(word).upper()
    word = " ".join(word.split())
    words = word.split(' ')
    for w in words:
        result = result + w[0]
    return result