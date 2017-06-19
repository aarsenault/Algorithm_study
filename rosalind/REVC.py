

file = open('rosalind_revc.txt', 'r')

input = file.readline()



def nucleotides(dna):
    """
    >>> nucleotides('AAAACCCGGT')
    'ACCGGGTTTT'

    """

    newstring = ''

    # reverse
    for i, ch in enumerate(dna):
        newstring = newstring + dna[-1 -i]

    # compliment
    newerstring = ''
    for charachter in newstring:
        if charachter is 'T':
            newerstring += 'A'
        if charachter is 'A':
            newerstring += 'T'
        if charachter is 'C':
            newerstring += 'G'
        if charachter is 'G':
            newerstring += 'C'
    return newerstring


test = False

if __name__ == "__main__":

    if test:
        import doctest
        doctest.testmod()
    else:

        results = open('results.txt', 'w+')

        results.write(nucleotides(input))

        results.close()

