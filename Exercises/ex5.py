from Compsci_II.Exercises.week6_heap import Heap


def merge_heap(heap1, heap2):
    '''
    (Heap, Heap) -> Heap
    '''
    curr_marz = heap1
    curr_nick = heap2
    if not curr_marz.is_empty() and not curr_nick.is_empty():

        my_dll = Heap(None)
        my_dll.extract_min()

        while not curr_marz.is_empty() or not curr_nick.is_empty():
            if not curr_marz.is_empty():
                temp = curr_marz.remove_last_node()
                my_dll.insert(temp)
            else:
                temp = curr_nick.remove_last_node()
                my_dll.insert(temp)

    elif curr_marz.is_empty() and not curr_nick.is_empty():
        my_dll = curr_nick

    elif not curr_marz.is_empty() and curr_nick.is_empty():
        my_dll = curr_marz

    else:
        my_dll = Heap(None)
        my_dll.extract_min()

    return my_dll


def first_and_last(heap):
    '''
    (Heap) -> tuple
    '''
    if not heap.is_empty():
        last = heap.remove_last_node()
        first = heap.extract_min()
        res = first, last
    else:
        res = Heap(None)
        res.extract_min()

    return res


if __name__ == "__main__":
    dl = Heap("Zse")
    names1 = sorted(["Archer", "Bailey", "Baker",
                     "Brewer", "Porter", "Potter",
                     "Sawyer", "Slater"])
    for name in names1:
        dl.insert(name)
    # Descending
    dl2 = Heap('Zsd')
    names2 = sorted(["Head", "Hunt", "Hunter",
                     "Judge", "Knight", "Miller",
                     "Mason", "Page", "Palmer",
                     "Parker", "Thatcher", "Turner",
                     "Walker", "Weaver"])
    for name in names2:
        dl2.insert(name)
    print(dl.size())
    print(dl2.size())
    print(dl.size() + dl2.size())
    l = merge_heap(dl, dl2)
    # print(l.BFS())
    a = Heap(None)
    b = Heap(None)
    a.extract_min()
    b.extract_min()
    z = merge_heap(a, b)
    print(l.BFS())
    print(l.size())
    # d1 = Heap(None)
    # d2 = Heap(None)
    # z = merge_heap(d1, d2)
    # print(z.BFS)
    g = first_and_last(l)
    print(g)
    # Ascending
    # x = reverse_merge(dl2, dl)
    # print(x)
    # print(x.size())
    # print(dl.size() + dl2.size())
    # z = DoubleLinkedList()
    # zi = ['Ahmed', 'Alex', 'Bevers', 'Bryan', 'Cai',
    #       'Chan', 'Ding', 'Do', 'Duong', 'Edwards', 'Elliott', 'Fan',
    #       'Franco',
    #       'Gallo', 'Han', 'Henderson', 'Hu', 'Joseph', 'Jung', 'Kang',
    #       'Lam', 'Lo', 'Lyn', 'Ma', 'McMurray', 'Muhammad',
    #       'Nathalia', 'Ning', 'Ou', 'Page', 'Peng', 'Qin', 'Ran',
    #       'Roy', 'Samara', 'Shah', 'Siu', 'Tam', 'Thomas', 'Tse',
    #       'Tu', 'Vance', 'Wan', 'Wong', 'Xia', 'Xu', 'Yao', 'Ye', 'Young',
    #       'Zhang']

    # for i in zi:
    #     z.add_last(i)

    # print(z)
    # y = allocate_room(z, "SW319", 10, 8)
    # print(y)
