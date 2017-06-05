
def quicksort(arr):
    """
    # test edge cases
    >>> quicksort([])
    []
    >>> quicksort([1])
    [1]

    # test sorting
    >>> quicksort([2, 1, 4, 3])
    [1, 2, 3, 4]
    >>> quicksort([2, 15, 89, 27, 16, 34, 120, 65, 51, 1, 54, 72, 210, 27])
    [1, 2, 15, 16, 27, 27, 34, 51, 54, 65, 72, 89, 120, 210]

    :param numbers: An array of numbers to be sorted
    :return: An array of inputs sorted smallest to largest

    """

    # create the base case
    if len(arr) in [0, 1]:
        return arr

        # perform partitioning on arrays > length 1

    # initialize the sub arrays
    smaller = []
    larger = []

    # choose the pivot at the end of the lists
    pivot = arr[-1]

    for value in arr[:-1]:
        if value < pivot:
            smaller.append(value)

        # equal numbers arbitrarily go in larger
        else:
            larger.append(value)

    sort_small = quicksort(smaller)
    sort_large = quicksort(larger)

    return sort_small + [pivot] + sort_large

if __name__ == "__main__":
    import doctest
    doctest.testmod()

