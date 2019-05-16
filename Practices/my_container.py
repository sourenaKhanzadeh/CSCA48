from abc import ABC, abstractclassmethod


class EmptyContainer(Exception):
    """raise an exception if queue is empty"""


class ContainerFullException(Exception):
    """raise if the Container is full"""


class Container(ABC):
    def __init__(self):
        '''
        (Container) -> NoneType
        '''
        self._container = []
        self.goal_word = []
        self._source_word = ''

    @abstractclassmethod
    def put(self, item):
        '''
        '''

    @abstractclassmethod
    def get(self):
        '''

        :return:
        '''

    @abstractclassmethod
    def move(self):
        '''
        '''

    def lenght(self):
        return len(self._container)

    def isempty(self):
        return self.lenght() == 0

    def getcontainer(self):
        return self._container

    def getgoal(self):
        return self.goal_word

    def setsourceword(self, source_word):
        self._source_word = source_word

    def getsourceword(self):
        return self._source_word


class Steue(ABC):
    def __init__(self):
        self._evenORodd = 0
        self._cont = []

    def insert(self, item):
        self._cont.append(item)

    def extract(self):
        if self._evenORodd % 2 == 0:
            res = self._cont.pop()
        else:
            res = self._cont.pop(0)

        self._evenORodd -= 1

        return res

    def isempty(self):
        return self.lenght() == 0

    def setevenORodd(self, num):
        self._evenORodd += num

    def lenght(self):
        return self._evenORodd

    def getcont(self):
        return self._cont


class Queue(Container):
    def put(self, item):
        self.getcontainer().insert(0, item)

    def move(self):
        if self.isempty():
            raise EmptyContainer("The Container Is Empty")
        else:
            self.getgoal().append(self.getcontainer()[0])

    def get(self):
        if self.isempty():
            raise EmptyContainer("The Container Is Empty")
        else:
            res = self.getcontainer().pop()

        return res


class Stack(Container):
    def put(self, item):
        self.getcontainer().append(item)

    def move(self):
        self.getgoal().append(self.getsourceword()[0])
        self.setsourceword(self.getsourceword()[1:])

    def get(self):
        if self.isempty():
            raise EmptyContainer("Container Is Empty")
        else:
            res = self.getcontainer().pop()

        return res


class Bucket(Container):
    def move(self):
        self.getgoal().append(self.getsourceword()[0])
        self.setsourceword(self.getsourceword()[1:])

    def get(self):

        if self.isempty():
            raise EmptyContainer("Container Is Empty")
        else:
            res = self.getcontainer().pop()
        return res

    def put(self, item):
        if self.lenght() == 0:
            self.getcontainer().append(item)
        else:
            raise ContainerFullException("The Container Is Full")


class QueueDict(Queue):
    def __init__(self):
        super().__init__()
        self._queue = {}
        self._start = 0
        self._end = 0

    def enque(self, item):
        super().put(item)
        self._queue[self._end] = item
        self._end += 1

    def dequeue(self):
        super().get()
        res = self._queue.pop(self._start)
        self._start += 1
        return res

    def getqueue(self):
        return self._queue

    def peek(self):
        return self.getqueue()[self._start]

    def lastitem(self):
        return self.getqueue()[self._end-1]


class QueueII:

    def __init__(self):
        # REPRESENTATION INVARIANT
        # _contents is a Steue
        # The elements in _contents are exactly
        # the elements in me
        self._contents = Steue()

    def enqueue(self, item):
        self._contents.insert(item)

    def dequeue(self):
        var = self._contents.extract()
        if not self.isempty():
            self.enqueue(var)
            res = self._contents.extract()
        else:
            res = var
        return res

    def isempty(self):
        return self._contents.isempty()

if __name__ == "__main__":
    print("---------QUEUE-------")
    myq = Queue()
    myq.put('A')
    myq.put('B')
    myq.put('C')
    print(myq.get())
    print(myq.get())
    print("---------Stack-------")
    myst = Stack()
    myst.put('A')
    myst.put('B')
    myst.put('C')
    print(myst.get())
    print(myst.get())
    print("---------BUCKET--------")
    myb = Bucket()
    myb.put('L')
    print(myb.getcontainer())
    print("---------QUEUEDICT-------")
    myqdict = QueueDict()
    myqdict.enque('A')
    myqdict.enque('B')
    myqdict.enque('C')
    myqdict.enque('D')
    myqdict.enque('E')
    print(myqdict.dequeue())
    print(myqdict.dequeue())
    print(myqdict.dequeue())
    print("---------STEUE-------")
    mysteue = Steue()
    mysteue.insert('A')
    mysteue.insert('B')
    mysteue.insert('C')
    mysteue.insert('D')
    mysteue.insert('E')
    print(mysteue.extract())
    print(mysteue.extract())
    print(mysteue.extract())
    print(mysteue.extract())
    print(mysteue.extract())
    print("---------QUEUEII-------")
    queueII = QueueII()
    queueII.enqueue("A")
    queueII.enqueue("B")
    queueII.enqueue("C")
    queueII.enqueue("D")
    queueII.enqueue("E")
    print(queueII.dequeue())
    print(queueII.dequeue())
    print(queueII.dequeue())
    print(queueII.dequeue())
    print(queueII.dequeue())

