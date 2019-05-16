def greeting(name):
    '''
    (str) -> str
    takes in a person's name and
    greets the person
    '''
    return "Hello {} how are you today?".format(name)


def mutate_list(listA):
    '''
    (list) -> NoneType
    mutates the list
    '''
    # iterate the list
    index_while = 1
    listA[0] = 'Hello'
    while index_while < len(listA):
        # find the index of the member
        i = index_while
        # if member of list is boolean
        if isinstance(listA[i], bool):
            # contradict it
            listA[i] = not listA[i]
        # if the member is integer
        elif isinstance(listA[i], int):
            # multiply by 2
            listA[i] = listA[i] * 2
        # if member is a string
        elif isinstance(listA[i], str):
            # take the first and last char
            j = list(listA[i])
            j.remove(j[0])
            j.remove(j[-1])
            listA[i] = "".join(j)
        index_while += 1


def merge_dicts(d1: dict, d2: dict) -> dict:
    '''
    (dict of {str: list of ints}, dict of {str: list of ints}) ->
    dict of {str: list of ints}
    insert to dictionaries and merged them together
    '''
    # check all the keys of the dictionaries
    dc1 = d1.copy()
    dc2 = d2.copy()

    for i in dc1:
        if i in dc2:
            var = dc1[i] + dc2[i]
            dc1[i] = var

    for j in dc2:
        if j not in dc1:
            dc1[j] = dc2[j]
    return dc1


if __name__ == "__main__":
    inputed_00 = [True, False, False]
    inputed_01 = [5, 7]
    inputed_02 = ["String", "sader", "olla", "holllow"]
    inputed_03 = [[1, 2, 3], 1, 2, 3]
    expected_00 = ["Hello", True, True]
    expected_01 = ["Hello", 14]
    expected_02 = ["Hello", "ade", "ll", "olllo"]
    expected_03 = ["Hello", 2, 4, 6]
    mutate_list(inputed_00)
    mutate_list(inputed_01)
    mutate_list(inputed_02)
    mutate_list(inputed_03)
    d1 = {'a': [1, 2, 3], 'b': [4], 'c': [5, 6, 7]}
    d2 = {'a': [2], 'b': [8, 9, 0], 'd': [10, 11, 12]}
    print(inputed_00 == expected_00)
    print(inputed_01 == expected_01)
    print(inputed_02 == expected_02)
    print(inputed_03 == expected_03)
    print(inputed_00)
    print(inputed_01)
    print(inputed_02)
    print(inputed_03)
    print(merge_dicts(d1, d2))
    print(merge_dicts(d2, d1))
