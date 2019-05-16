from Compsci_II.Exercises.week6_heap import Heap
from Compsci_II.Lectures.week4.DLL import *
import time

a = time.clock()


def reverse_merge(dll_marz, dll_nick):
    '''
    (DLL, DLL) -> DLL
    Takes in two double linked
    list that represents the surname
    of Marziehs and Nicks students in
    descending order then merges them
    in an ascending order.
    REQ: DLL's can be any length
    REQ: Surnames must be different
    '''
    curr_marz = dll_marz.remove_first()
    curr_nick = dll_nick.remove_last()

    my_dll = DoubleLinkedList()

    # while the first element from marzias and last
    # element from nicks exist run this
    while curr_marz is not None and curr_nick is not None:
        # if marz element is bigger then
        # add marziehs curr and make curr nick the
        # same thing
        if curr_marz > curr_nick:
            my_dll.add_last(curr_nick)
            curr_nick = dll_nick.remove_last()
        # if nicks element is bigger do the same
        # with marziehs
        elif curr_marz < curr_nick:
            my_dll.add_last(curr_marz)
            curr_marz = dll_marz.remove_first()
        # if marz and nick have the same student
        # remove from marz add to output dll
        # remove from nick
        else:
            curr_marz = dll_marz.remove_first()
            my_dll.add_last(curr_nick)
            curr_nick = dll_nick.remove_last()
    # if marz is empty
    if curr_marz is None:
        # add all nicks student to the output
        while curr_nick is not None:
            my_dll.add_last(curr_nick)
            curr_nick = dll_nick.remove_last()
    # if nick is empty
    elif curr_nick is None:
        # add all of marz in the list
        while curr_marz is not None:
            my_dll.add_last(curr_marz)
            curr_marz = dll_marz.remove_first()

    return my_dll

b = time.clock()


def allocate_room(r_name, r_number, cap, index):
    '''
    (DLL, str, int, int) -> str
    insert the list of students, room number
    and the room capacity and the index of the
    students desired for that room and return
    the string representation of the room and the
    first two letter's of the first and last name
    in this format: let first and last letters be
    represented as x and y respectively then xx-yy
    REQ: if n rooms and m students and m <= n then
    all the desired students are allowed
    '''
    # these are going to be the
    # first two letters of first and
    # last name respectively
    end, cur = '', ''
    total_size = r_name.size() + index
    # starts from index 1
    a = -1
    # if there is more than 1 people and
    # the capacity the room is more than 1
    if r_name.size() != 1 and cap != 1:

        while a < index:
            # remove the first until we
            # get to the data
            if r_name.get_first() is not None:
                # we have our first person name
                cur = r_name.remove_first()
            a += 1

        a = 1
        while a < cap:
            # as long as there is an element
            # and does not equal to None
            if r_name.get_first() is not None:
                # if the capacity of the room
                # is less than the number of students
                # remove the first student after our
                # index until the room capacity is full
                if cap < r_name.size():
                    end = r_name.remove_first()
                else:
                    end = r_name.remove_last()
                    a += cap
            a += 1

    else:
        # if the room capacity or the
        # number of students is equal to 1
        # return the first student as both
        # last and first person
        end = r_name.remove_first()
        cur = end

    return r_number + " " + str(cur[:2]).upper() + '-' + str(end[:2]).upper()
c = time.clock()


def merge_heap(heap1, heap2):
    '''
    (Heap, Heap) -> Heap
    '''
    curr_marz = heap1
    curr_nick = heap2
    if not curr_marz.is_empty() and not curr_nick.is_empty():

        my_dll = Heap(heap1.extract_min())
        while not curr_marz.is_empty() or not curr_nick.is_empty():
            if not curr_marz.is_empty():
                temp = curr_marz.extract_min()
                my_dll.insert(temp)
            else:
                temp = curr_nick.extract_min()
                my_dll.insert(temp)
    else:
        my_dll = Heap(None)

    return my_dll

d = time.clock()


def first_and_last(heap):
    '''
    (Heap) -> tuple
    '''
    last = heap.remove_last_node()
    first = heap.extract_min()
    return first, last

e = time.clock()

if __name__ == "__main__":
    dl = Heap("Arman")
    names1 = sorted(["Archer", "Bailey", "Baker",
                     "Brewer", "Porter", "Potter",
                     "Sawyer", "Slater",
                     "Smith", "Stringer", "Taylor",
                     "Butcher", "Carter", "Chandler",
                     "Clark", "Collier"])
    for name in names1:
        dl.insert(name)
    # Descending
    dl2 = Heap('Dilon')
    names2 = sorted(["Head", "Hunt", "Hunter",
                     "Judge", "Knight", "Miller",
                     "Mason", "Page", "Palmer",
                     "Parker", "Thatcher", "Turner",
                     "Walker", "Weaver"])
    for name in names2:
        dl2.insert(name)

    l = merge_heap(dl, dl2)
    print(d-c)
    print(l.BFS())
    # print(l.BFS())
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


if __name__ == "__main__":
    dl = DoubleLinkedList()
    names1 = sorted(["Archer", "Bailey", "Baker",
                     "Brewer", "Porter", "Potter",
                     "Sawyer", "Slater",
                     "Smith", "Stringer", "Taylor",
                     "Butcher", "Carter", "Chandler",
                     "Clark", "Collier"])
    for name in names1:
        dl.add_first(name)
    # Descending
    dl2 = DoubleLinkedList()
    names2 = sorted(["Head", "Hunt", "Hunter",
                     "Judge", "Knight", "Miller",
                     "Mason", "Page", "Palmer",
                     "Parker", "Thatcher", "Turner",
                     "Walker", "Weaver"], reverse=True)
    for name in names2:
        dl2.add_first(name)
    # Ascending
    x = reverse_merge(dl2, dl)
    print(b-a)
    print(x)
    print(x.size())
    # print(dl.size() + dl2.size())
    z = DoubleLinkedList()
    zi = ['Ahmed', 'Alex', 'Bevers', 'Bryan', 'Cai',
          'Chan', 'Ding', 'Do', 'Duong', 'Edwards', 'Elliott', 'Fan',
          'Franco',
          'Gallo', 'Han', 'Henderson', 'Hu', 'Joseph', 'Jung', 'Kang',
          'Lam', 'Lo', 'Lyn', 'Ma', 'McMurray', 'Muhammad',
          'Nathalia', 'Ning', 'Ou', 'Page', 'Peng', 'Qin', 'Ran',
          'Roy', 'Samara', 'Shah', 'Siu', 'Tam', 'Thomas', 'Tse',
          'Tu', 'Vance', 'Wan', 'Wong', 'Xia', 'Xu', 'Yao', 'Ye', 'Young',
          'Zhang']

    for i in zi:
        z.add_last(i)

    print(z)
    y = allocate_room(z, "SW319", 10, 8)
    print(y)
