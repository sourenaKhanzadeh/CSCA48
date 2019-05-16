class DLLnode:
    """ A node for a doubly linked list of objects."""
    def __init__(self: 'DLLnode', data: object,
        prev: 'DLLnode' or None, nxt: 'DLLnode' or None) -> None:
        self.data = data
        self.prev = prev
        self.nxt = nxt


def shuffle(head: 'DLLnode') -> 'DLLnode':
    """
    Shuffle the doubly linked list whose first node is head.
    Return the head of the updated list.
    """
    # if list not empty
    if head is not None:
        # set before, curr to point at first, second node respectively
        prev = head
        curr = head.nxt
        # shuffle 2 nodes at a time until end of list
    while curr is not None:
        # set what should point to curr
        if head.nxt != None:
            __________ . __________ . __________ = __________
        else:
            __________ = __________
    # set forward pointers
    __________ . __________ = __________ . __________
    __________ . __________ = __________
    # loop continues on next page
    # fill in each blank with one of:
    # before, curr, prev, nxt, head, None
    # set what should point back to before
    if __________.__________ != __________:
        __________.__________.__________ = __________
    # set backward pointers
    __________.__________ = __________.__________
    __________.__________ = __________
    # advance before and curr to next pair of nodes
    __________ = __________.__________
    if __________ != __________:
        __________ = __________.__________
    else:
        __________ = __________
    return __________

if __name__ == "__main__":
    dl = DLLnode(None, None, None)

