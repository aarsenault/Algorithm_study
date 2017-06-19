

file = open('rosalind_rna.txt', 'r')


content = file.readline()



def nucleotides(dna):
    """
    >>> nucleotides('GATGGAACTTGACTACGTAAATT')
    'GAUGGAACUUGACUACGUAAAUU'

    """



    newstring = ''

    for charachter in dna:
        if charachter is not 'T':
            newstring += charachter
        if charachter is 'T':
            newstring += 'U'
    return newstring


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()


print(nucleotides(content))
