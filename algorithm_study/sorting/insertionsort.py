#!/bin/python

# m = input()
# ar = [int(i) for i in raw_input().strip().split()]
# insertionSort(ar)


"""
Nothing in here will get run
x = 5

"""



#  expected input
# 5

array =  [2, 4, 6, 8, 3 ]


# expected output
# 2 4 6 8 8
# 2 4 6 6 8
# 2 4 4 6 8
# 2 3 4 6 8


def insertionSort(ar):

    last_elem = ar[-1]

    for i in range(len(ar)):
        # 0

        if last_elem < ar[i]:

        else:
            # insertion
            ar[-2] = last_elem

    return ar


print(insertionSort(array))
