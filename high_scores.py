puntajes = [1,2,3,4,5,6,7,8,9,10]

def highest_score(lista = puntajes):
    if not isinstance(lista, list):
        raise Exception("You must enter a list")
    lista.sort(reverse=True)
    return lista[0]

def three_highest_scores(lista = puntajes):
    if not isinstance(lista, list):
        raise Exception("You must enter a list")
    lista.sort(reverse=True)
    return lista[0:3]
