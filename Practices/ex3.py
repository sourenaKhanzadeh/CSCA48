from container import *


class NeckQueue(Queue):
    def dequeue(self):
        # if queue not empty then pop
        # the element
        if self.is_empty():
            quit()
        first_item = super().dequeue()
        # this means that there is one element
        if self.is_empty():

            ret_item = first_item
        # if there is more than one item
        # then return the second item and
        # put back the first item
        else:
            ret_item = super().dequeue()
            self.enqueue(first_item)

        return ret_item


if __name__ == "__main__":
    ne = NeckQueue()
    ne.enqueue(1)
    ne.enqueue(2)
    ne.enqueue(3)
    ne.enqueue(4)
    ne.enqueue(5)
    ne.enqueue(6)
    ne.enqueue(7)
    ne.enqueue(8)
    for i in range(ne.size()):
        print(ne.dequeue())
        '''___________________________container_-_-_-_-_-_-_Print
       ne.deque   1 ---> back       3 4 5 6 7 8 1               2
       ne.deque   3 ---> back       5 6 7 8 1 3                 4
       ne.deque   5 ---> back       7 8 1 3 5                   6
       ne.deque   7 ---> back       1 3 5 7                     8
       ne.deque   1 ---> back       5 7 1                       3
       ne.deque   5 ---> back       1 5                         7 
       ne.deque   1 ---> back       1                           5
       ne.deque   1 ---> one_item                               1
       '''
