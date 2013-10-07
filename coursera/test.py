def count_repeats(s):
    '''
    >>> s = 'asdfgteehhtt'
    >>> count_repeats(s)
    3
    >>> s = 'aaaaa'
    >>> count_repeats(s)
    4
    '''
    repeats = 0

    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            repeats = repeats + 1

    return repeats


def shift_left(L):
    '''
    >>> L = ['a', 'b', 'c', 'd']
    >>> shift_left(L)
    >>> print(L)
    ['b', 'c', 'd', 'a']
    '''
    first_item = L[0]

    for i in range(1, len(L)):
        L[i-1] = L[i]
    L[-1] = first_item


def sum_items(list1, list2):
    '''
    >>> sum_items([2, 3], [2, 3])
    [4, 6]
    >>> list1 = [3, 4, 5]
    >>> list2 = [5, 4, 3]
    >>> sum_items(list1, list2)
    [8, 8, 8]
    '''
    sum_list = []

    for i in range(len(list2)):
        sum_list.append(list1[i] + list2[i])

    return sum_list

def count_matches(s1, s2):
    '''
    >>> s1 = 'ape'
    >>> s2 = 'ate'
    >>> count_matches(s1, s2)
    '''
    num_matches = 0

    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1

    return num_matches


def calculate_average(asn_grades):
    '''
    >>> asn_grades = [['assignment1', 70], ['assignment2', 80]]
    >>> calculate_average(asn_grades)
    75.0
    '''
    total = 0

    for item in asn_grades:
        total = total + item[1]

    return total / len(asn_grades)


def averages(grades):
    '''
    >>> grades = [[50, 60, 40], [30, 55, 70], [30, 80]]
    >>> averages(grades)
    [50.0, 51.666666666666664, 55.0]
    '''
    averages = []

    for grades_list in grades:

        total = 0
        for mark in grades_list:
            total = total + mark

        averages.append(total / len(grades_list))

    return averages
        

    














        

    
    
