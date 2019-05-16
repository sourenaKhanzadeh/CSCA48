def rsum(my_l):
    '''
    (list) -> int
    returns the sum of
    all the elements in
    the list
    >>> l = [1,2,34]
    >>> rsum(l)
    37
    >>> l = [1,2,34,23]
    >>> rsum(l)
    60
    >>> l = [1,2]
    >>> rsum(l)
    3
    >>> l = [1]
    >>> rsum(l)
    1
    '''
    if len(my_l) == 0:
        result = 0
    else:
        first = my_l[0]
        my_l = my_l[1:]
        l = rsum(my_l)
        result = first + l

    return result


def rmax(my_l):
    '''
    (list) -> int
    returns the maximum
    number in the list
    >>> l = [1,2,3,4,5,6,7]
    >>> rmax(l)
    7
    '''
    if len(my_l) == 1:
        res = my_l[0]
    else:
        first = my_l[0]
        my_l = my_l[1:]
        l = rmax(my_l)
        if first > l:
            first = first
        else:
            first = l

        res = first

    return res


def rmin(my_l):
    '''
    (list) -> int
    return the smallest
    number in the list
    '''

    if len(my_l) == 1:
        res = my_l[0]
    else:
        first = my_l[0]
        my_l = my_l[1:]
        l = rmin(my_l)
        if first < l:
            first = first
        else:
            first = l

        res = first

    return res


def second_smallest(my_l):
    '''
    (list) -> int
    returns the second smallest number
    in the list
    >>> l = [1,2,3,4,5]
    >>> second_smallest(l)
    2
    >>> l = [1,2,3,4,5]
    >>> second_smallest(l)
    2
    >>> l = [1,12,234,54,476,2,42]
    >>> second_smallest(l)
    2
    >>> l = [0,12,124,35,1,2,3,4,5,234,45,645]
    >>> second_smallest(l)
    1
    '''
    my_l = my_l[:]
    my_l.pop(my_l.index(rmin(my_l)))
    return rmin(my_l)


def sum_max_min(my_l):
    '''
    (list) -> int
    returns the sum of the
    maximum and the minimum in
    the list
    >>> l = [1,2,3,4,5]
    >>> sum_max_min(l)
    6
    >>> l = [1,3,4,5,2]
    >>> sum_max_min(l)
    6
    >>> l = [1,12,234,54,476,2,42]
    >>> sum_max_min(l)
    477
    >>> l = [12,124,35,1,2,3,4,5,234,45,645]
    >>> sum_max_min(l)
    646
    '''
    return rmax(my_l) + rmin(my_l)

if __name__ == "__main__":
    l = [111111, 22435, 356, 857, 869, 2356]
    print(sum_max_min(l))
    print(rmax(l))
    print(l)
    print(rmax([-1, -3, -4]))
