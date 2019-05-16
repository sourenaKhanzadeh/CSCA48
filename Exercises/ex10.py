container = {i: [] for i in range(10)}
z = []


def radix_sort(l):
    """
    (list of ints) -> list of ints
    """
    x = radix_sort_a(l)[:]
    z.clear()
    return x


def radix_sort_a(l):
    """
    (list of ints) -> list of ints
    """
    for i in range(len(l)):
        cont(str(l[i])[-1], l[i])
    x = not_sorted(container)
    index = 0
    while x:
        index += 1
        empty(container, l)
        sort_it(l, index)
        x = not_sorted(container)
    for i in container[0]:
        z.append(i)

    return z


def cont(l, l2):
    """
    """
    for i in container:
        if l == str(i):
            container[i].append(l2)


def not_sorted(l):
    x = False
    if len(l[0]) != 0:
        x = True
    for i in l:
        if i != 0 and len(l[i]) != 0:
            x = True
    return x


def sort_it(l, index):
    """
    """
    for i in range(len(l)):
        if len(str(l[i]))-1 >= index:
            cont(str(l[i])[len(str(l[i]))-index-1], l[i])
        else:
            z.append(l[i])


def empty(l, l2):
    l2.clear()
    for i in l:
        while len(l[i]) != 0:
            l2.append(l[i].pop(0))

if __name__ == "__main__":
    # import random
    # k = random.sample(range(300), 20)
    x = radix_sort([1, 203, 10, 900, 4, 90,  5, 20, 30])
    # g = radix_sort(k)
    print(x)
    # print(g)
