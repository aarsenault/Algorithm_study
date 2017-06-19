

dna_file = open('rosalind_dna.txt', 'r')


content = dna_file.readline()



def nucleotides(dna):
    """
    >>> nucleotides('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
    '20 12 17 21'

    """


    A = 0
    C = 0
    G = 0
    T = 0


    for charachter in dna:
        if charachter is 'A':
            A += 1
        if charachter is 'C':
            C += 1
        if charachter is 'G':
            G += 1
        if charachter is 'T':
            T += 1
    return '{} {} {} {}'.format(A, C, G, T)


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()


print(nucleotides(content))
