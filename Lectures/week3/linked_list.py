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

Infinite lists
--------------

Regardless, it is problematic that we cannot prove that
print_list and print_backward terminate. The best we
can do is the hypothetical statement, “If the list
contains no loops, then these methods will terminate.”
This sort of claim is called a precondition. It imposes
a constraint on one of the parameters and describes the
behavior of the method if the constraint is
satisfied. You will see more examples soon.

The fundamental ambiguity theorem
----------------------------------

head = list
tail = list.next


'''


def bc_word(x):
    if x is not None: return
    y = x[::-1]
    bc_word(x)
    print(y)


def count_down(n):
    if n == 0:
        print("blast off")
    else:
        print(n)
        count_down(n-1)


bc_word('wsdfasf')
count_down(100)