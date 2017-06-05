import sys





def heapsort(arr):
    """Given an unsorted list, return a sorted list via a heap sort."""

    arr_size = len(arr)
    # siftDown() nodes (not leaves) from bottom to top
    #   arr_size / 2 is the last node of a binary tree so we start there
    # For siftDown:
    #   current node index is considered "root"
    #   sifts all the way down (last list index is considered "bottom")
    for i in list(reversed(range(0, int(arr_size / 2)))):
        arr = siftDown(arr, i, arr_size - 1)

    for i in list(reversed(range(1, arr_size))):
        arr[0], arr[i] = arr[i], arr[0]

        # Sift down from root to end of unsorted portion of list
        arr = siftDown(arr, 0, i - 1)

    return arr


def siftDown(arr, root, bottom):
    # While root has at least 1 child
    while (root * 2 + 1 <= bottom):

        # maxChild: Compare node's 2 children and set maxChild to index of
        # child w/ larger value

        # Find maxChild
        # Only 1 child, so it becomes maxChild
        if (root * 2 + 1 == bottom):
            maxChild = root * 2 + 1
        elif (arr[root * 2 + 1] > arr[root * 2 + 2]):
            maxChild = root * 2 + 1
        else:
            maxChild = root * 2 + 2

        # if child is larger, swap child and root
        # and run again based on the original root's new index
        if (arr[root] < arr[maxChild]):
            arr[root], arr[maxChild] = arr[maxChild], arr[root]
            root = maxChild
        else:
            # We're done here
            break
    return arr


if __name__ == '__main__':
    arr = list(map(int, sys.argv[1].split(',')))
    print(heapsort(arr))