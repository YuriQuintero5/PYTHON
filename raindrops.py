def raindrops(number=''):
    resultado = ''
    number = str(number)
    if(number.isnumeric()):
        n = int(number)
        if(n % 3 == 0):
            resultado += 'Pling'
        if (n % 5 == 0):
            resultado += 'Plang'
        if (n % 7 == 0):
            resultado += 'Plong'
        if(len(resultado) == 0):
            resultado += number
        return resultado
    else:
        #raise Exception("You must enter a numeric value")
        return "You must enter a numeric value"
