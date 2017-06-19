
# n is sequence index, k is the number of offspring

def fibonacci(n, k):
    """
    >>> fibonacci(5, 3)
    19


    :param n:
    :return:
    """
    if n == 0:
        return 1
    else:
        return fibonacci((n-1),k) + fibonacci((n-1),k)*k


if __name__ == "__main__":
    import doctest
    doctest.testmod()
