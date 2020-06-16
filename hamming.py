def hamming(dna1, dna2):
    if(len(dna1) == len(dna2)):
        distance = 0
        for i in range(len(dna1)):
            if(dna1[i] != dna2[i]):
                distance = distance + 1
        return 'The Hamming Distance is {}'.format(distance)
    else:
        raise Exception("The sequences are of different lengths")
