'''

Glossary
--------
constant time
An operation whose runtime does not depend on the size of the data structure.

FIFO (First In, First Out)
a queueing policy in which the first member to arrive is the first to be removed.

linear time
An operation whose runtime is a linear function of the size of the data structure.

linked queue
An implementation of a queue using a linked list.

priority queue
A queueing policy in which each member has a priority determined
by external factors. The member with the highest priority is the first to be removed.

Priority Queue
An ADT that defines the operations one might perform on a priority queue.

queue
An ordered set of objects waiting for a service of some kind.

Queue
An ADT that performs the operations one might perform on a queue.

queueing policy
The rules that determine which member of a queue is removed next.

• Data:
    • Any arbitrary objects/elements

• Operations:
    • Main:
        • enqueue(e): add element e to the back/tail of the queue
        • dequeue(): remove and return the element from the front/head of the queue
    • Auxiliary:
        • front(): returns the element at the front without removing it
        • size(): returns the number of elements in the queue
        • is_empty(): indicates whether or not the queue is empty

• Exception:
    • Raise EmptyQueueException if the queue is empty and dequeue() or front() is
    requested

'''


class EmptyQueueException(Exception):
    pass


class Queue:
    ''' this class defines a Queueu ADT and raises an
     exception in case the queue is empty and dequeue() or front() is requested'''

    def __init__(self):
        '''(Queue) -> Nonetype
        creates an empty queue'''
        # representation invariant
        # _queue is a list
        # if _queue is not empty then
        #    _queue[0] referes to the front/head of the queue
        #    _queue[:-1] referes to the back/tail of the queue
        #    _queue[:] referes to the elements of the queue in the order of insertion
        self._queue = []

    def enqueue(self, element):
        ''' (Queue, obj) -> NoneType
        add element to the back of the queue'''
        # The element goes to the back of queue
        self._queue.append(element)

    def dequeue(self):
        '''(Queue) -> obj
        remove and returns the element at the front of the queue
        raise an exception if _queue is empty'''
        if self.is_empty():
            raise EmptyQueueException("This queue is empty")
        # remove and return the item at the front
        return self._queue.pop(0)

    def is_empty(self):
        ''' (Queue) -> bool
        returns true if _queue is empty'''
        return len(self._queue) == 0

    def size(self):
        '''(Queue) -> int
        returns the number of elements, which are in _queue'''
        return len(self._queue)

    def front(self):
        '''(Queue) -> obj
        returns the first element, which is in _queue
        It raises an exception if this queue is empty'''
        if self.is_empty():
            raise EmptyQueueException("This Queue is Empty")
        return self._queue[0]

if __name__ == "__main__":
    queue = Queue()
