count1 = 0
claim = set()
res = set()
x = 0


def edit_distance(s1, s2):
    """
    (str, str) -> int
    """
    if len(s1) == 0 and len(s2) == 0:
        result = 0
    elif len(s1) == 1 and len(s2) == 1:
        if s1[0] == s2[0]:
            result = 0
        else:
            result = 1
    else:
        if s1[0] == s2[0]:
            result = edit_distance(s1[1:], s2[1:])
        else:
            result = 1 + edit_distance(s1[1:], s2[1:])
    return result


def subsequences_helper(s1, s2):
    """
    (str, str) -> bool
    """
    if len(s2) == 0:
        s2 = ''
    elif len(s2) == 1:
        if not s2[0] in s1:
            s2 = s2.replace(s2[0], '')
    else:
        s2 = s2[0] + subsequences_helper(s1, s2[1:])
        if not s2[0] in s1:
            s2 = s2.replace(s2[0], '')
    return s2


def subsequence(s1, s2):
    """
    (str, str) -> bool
    """
    result = subsequences_helper(s1, s2)
    return s1 == result


def perms(s):
    """
    (str) -> set of {str}
    """
    if len(s) <= 1:
        return {s}
    permSet = set()
    for i, c in enumerate(s):
        newStr = remove_char(s, i)
        retSet = perms(newStr)
        for elem in retSet:
            permSet.add(c + elem)
    return permSet


def remove_char(s, index):
    endIndex = index if index == len(s) else index + 1
    return s[:index] + s[endIndex:]


if __name__ == '__main__':
    # import time as t
    print(edit_distance('crsete', 'secret'))
    print(subsequence('dog', 'XYZdABCo123g!!!'))
    # a = t.clock()
    print(perms('str'))
    # b = t.clock()
    # print(b-a)
