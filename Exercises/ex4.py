total = []


class Node:
    '''A node in a linked list'''

    def __init__(self, data, next_node=None):
        '''
        (Node) -> NoneType
        '''
        self.data = data
        self.next_node = next_node


class Stack:
    '''A stack of objects'''

    def __init__(self):
        '''
        (Stack) -> NoneType
        '''
        self._container = []

    def push(self, my_object):
        '''
        (Stack, obj) -> NoneType
        add's element at the top of
        the container
        '''
        self._container.append(my_object)

    def pop(self):
        '''
        (Stack) -> NoneType
        return the element at the
        top of the container
        '''
        return self._container.pop()

    def is_empty(self):
        '''
        (Stack) -> bool
        returns true if the stack
        is empty
        '''
        return self.length() == 0

    def length(self):
        '''
        (Stack) -> int
        return's the number of
        elements in the container
        '''
        return len(self._container)

    def get(self):
        '''
        (Stack) -> list
        gets the container
        '''
        return self._container


stack = Stack()


def sum(node: object):
    '''
    (Node or NoneType) -> int
    gives the sum of all nodes
    '''
    if node.next_node is not None:
        first_sum = node.data
        total.append(first_sum)
        sum(node.next_node)
    if node is not None and node.next_node is None:
        total.append(node.data)

    return add(total)


def add(tot):
    '''
    (list) -> int
    gives the sum of
    all elements in the list
    '''
    tot = tot[:]
    z = 0
    for i in range(len(tot)):
        z += tot.pop()
    return z


def reverse(node: object):
    '''
    (Node) -> Node
    returns the reverse of the linked
    nodes
    '''
    stacks = stack_nodes(node)
    for j in range(len(stacks)):
        if stacks[j-1] in stacks:
            stacks[j].next_node = stacks[j-1]
    node.next_node = None
    return stacks[-1]


def stack_nodes(node: object):
    '''
    (Node or NoneType) -> list
    stacks the nodes
    '''
    if node is not None:
        stack.push(node)
        stack_nodes(node.next_node)

    return stack.get()


def splice(node: object, i: int):
    '''
    (Node or NoneType, int) -> Node
     splices the node
    '''
    global my_list
    stacks = stack_nodes(node)
    if i in range(len(stacks)):
        stacks[-1].next_node = stacks[0]
        first = stacks[:i]
        second = stacks[i:]
        my_list = second + first
        my_list[-1].next_node = None

    return my_list[0]


if __name__ == '__main__':
    n1 = Node(12)
    n2 = Node(54)
    n3 = Node(25)
    n4 = Node(34)
    n5 = Node(11)
    n6 = Node(22)
    n7 = Node(345)
    n1.next_node = n2
    n2.next_node = n3
    n3.next_node = n4
    n4.next_node = n5
    n5.next_node = n6
    n6.next_node = n7
    x = sum(n1)
    y = reverse(n1)
    z = splice(n1, 2)
    print(x)
    print(y.data)
    print(z.data)
