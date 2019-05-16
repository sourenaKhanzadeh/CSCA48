'''
Linked lists
------------

Linked lists are made up of nodes, where each node contains a
reference to the next node in the list. In addition, each
node contains a unit of data called the cargo.

A linked list is considered a recursive
data structure because it has a recursive definition.

The Node class
--------------
# >>> node1 = Node(1)
# >>> node2 = Node(2)
# >>> node3 = Node(3)

To link the nodes, we have to make
the first node refer to the second
and the second node refer to the third:

# >>> node1.next = node2
# >>> node2.next = node3

Lists as collections
--------------------
Lists are useful because they
provide a way to assemble multiple objects into
a single entity, sometimes called a collection.
In the example, the first node of the list serves
as a reference to the entire list.

To pass the list as a parameter, we only have to pass a reference to
the first node. For example, the function print_list
takes a single node as an argument. Starting with the
head of the list, it prints each node until it gets to the end:

def print_list(node):
    while node is not None:
        print(node, end=" ")
        node = node.next
    print()

Lists and recursion
-------------------
It is natural to express many list operations using
recursive methods. For example, the following is a
recursive algorithm for printing a list backwards:

'''


def bc_word(x, y):
    if x is not None: return
    y = x[::-1]
    bc_word()
    print(y)

bc_word('wsdfasf', 'sfafds')