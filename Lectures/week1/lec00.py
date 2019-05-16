'''
client-server-model
-------------------
server - provides a service
Client - uses the service

Modular Design
--------------

Encapsulation/ Data Hiding
--------------------------
all relevant things in a module
putting things that are
related all in the same place

. data must be hidden
. private/public variables

Python - use a convention(set of rules that everyone agrees to) self._y = 1 is private
------

Abstract Data Type(ADT)
----------------------
. boiled down to the essential's
. you want to make your data type as general as possible
. the operation's that can be performed on the data
. errors that can be generated

S/W(software) reuse
-------------------
if you make it as general as possible it will make it easier to reuse

Line-up
-------
First In First out(FIFO)
. Queue

Miscellaneous
--------------
the design must be good
enough to change it when needed

Definition of a queue
---------------------
Data: a sequence of objects
. object's are removed in the order they are inserted
. first object is called "Head"
. last object is called "Tail"

Operations
----------
_enqueue():
. Append object to queue
_deque():
. Remove and return the object in queue
. REQ: the queue must be not empty
_isEmpty():
. Return whether queue is empty

Abstract Base Class(ABC)
------------------------

'''

'''
• Abstract classes inherits from ABC (Abstract Base Classes) module in
Python.
• At least one of the methods should be decorated with
@abstractmethod
• An abstract class can contain both abstract and non-abstract method
• An abstract method must be overrriden in all of the subclasses
'''


# A queue class (not python's queue)
# Uses a list for the queue.


class Queue():
    def __init__(self: 'Queue') -> None:
        # Representation invariant:
        # _contents is a list.
        # len(_contents) is the number of elements in me.
        # If len(_contents)>0, then
        #   _contents[0] is the head,
        #   _contents[-1] is the tail,
        #   _contents[:] contains
        #    the elements in the order they were inserted.
        self._contents = []

    def __str__(self: 'Queue') -> str:
        s = ""
        for item in self._contents:
            s = s + str(item) + ", "
        return s[:-2]

    def enqueue(self: 'Queue', item: 'object') -> None:
        self._contents.append(item)

    def dequeue(self: 'Queue') -> object:
        return self._contents.pop(0)

    def isempty(self: 'Queue') -> bool:
        return len(self._contents) == 0

# A class for a checkout line
# Uses a list for the line.
# WARNING: contains poor code.


class CheckoutLine:
    def __init__(self: 'CheckoutLine') -> None:
        self.line = []

    def arrive(self: 'CheckoutLine', customer: str) -> None:
        self.line.append(customer)

    def depart(self: 'CheckoutLine') -> str:
        customer = self.line[0]
        del self.line[0]
        return customer

# program to simulate a checkout line
# WARNING: contains poor code.


def line2str(line):
    s = ""
    for customer in line:
        s = s + customer + ", "
    s = s[:-2]
    return s

my_checkout = CheckoutLine()
input("Customer Alice arriving...")
my_checkout.arrive("Alice")
input("Here's the line: " + line2str(my_checkout.line))

input("Customer Bob arriving...")
my_checkout.arrive("Bob")
input("Here's the line: " + line2str(my_checkout.line))

input("A customer departing...")
customer = my_checkout.depart()
input("It was customer " + customer)
input("Here's the line: " + line2str(my_checkout.line))

input("Customer Carole arriving...")
my_checkout.arrive("Carole")
input("Here's the line: " + line2str(my_checkout.line))

input("A customer departing...")
customer = my_checkout.depart()
input("It was customer " + customer)
input("Here's the line: " + line2str(my_checkout.line))

input("A customer departing...")
customer = my_checkout.depart()
input("It was customer " + customer)
input("Here's the line: " + line2str(my_checkout.line))
