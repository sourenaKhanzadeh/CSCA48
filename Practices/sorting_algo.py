cont = [[] for i in range(10)]
temp = []


def radix_sort(L):
    """
    sorting algo using
    radix sort
    """
    index = -1


def put(L, n):
    """
    fit in cont
    """
    for i in L:
        cont[int(str(i)[n])].append(i)


def take(L):
    """
    stores in a temporary
    list
    """
    for i in L:
        while len(i) != 0:
            temp.append(i.pop(0))


def bubble_sort(L):
    for i in L:
        curr = i
        if L.index(i) + 1 < len(L) -1:
            nex = L[L.index(i) + 1]
        index = 1
        while curr > nex:
            print("fuck")
            if curr > nex and index < len(L):
                L[index] = curr
                L[index - 1] = nex
                index += 1 if index < len(L)-1 else 0

                nex = L[index]

    return L

if __name__ == "__main__":
    from random import randint
    x = [randint(0, 300) + 1 for i in range(10)]
    # x.sort(reverse=True)
    # put(x, -1)
    # print(cont)
    # take(cont)
    # print(temp)
    print(bubble_sort(x))
