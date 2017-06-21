"""
Function to add all n previous numbers of some positive integer N
so long as n is not divisible by 5
"""



def hasfive(number):
    while number > 0:
        if number % 5 == 0 and number % 10 != 0:
            return True
        number = number // 10
    return False

def nofivecounter(start, stop):
    count = 0
    for number in range(start, stop + 1):
        if not hasfive(number):
            # print(number)
            count += 1
    return count
