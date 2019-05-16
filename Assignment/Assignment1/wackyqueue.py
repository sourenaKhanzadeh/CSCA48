"""
# Copyright Nick Cheng, 2018
# Copyright Sourena Khanzadeh, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2018
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""
from wackynode import WackyNode


class WackyQueue:
    """The Class WackyQueue"""

    def __init__(self):
        # REPRESENTATION INVARIANTS
        # _head_even is the head of the even linked list
        # initially set to None
        # _head_odd si the head of odd linked list
        # initially set to None
        # if WackyQueue is not empty
        #    then the _head_odd is the first element
        #    of our list
        #
        # if WackyQueue is not empty and extracthigh
        #     _head_odd is the first to be removed
        # if negate all and 1 item in WackyQueue
        #       negate the <pri> of _head_odd only
        self._head_even = None
        self._head_odd = None

    def __str__(self):
        '''
        (WackyQueue) -> str
        This is the string representation
        of this class where it returns
        the relationship between the linked lists
        '''
        curr_even = self.getevenlist()
        curr_odd = self.getoddlist()
        order_even = ''
        order_odd = ''
        # as long as curr is not Null
        # if the next node is not null
        # add the item of the node and point
        # to the second item
        # if it is the last node point it to
        while curr_even:
            if curr_even.get_next():
                order_even += str(curr_even.get_item())\
                              + '|' + str(curr_even.get_priority()) + ' --> '
            else:
                order_even += str(curr_even.get_item()) +\
                              '|' + str(curr_even.get_priority()) + ' --> NONE'

            curr_even = curr_even.get_next()

        # Do the same thing but for the odd list
        while curr_odd:
            if curr_odd.get_next():
                order_odd += str(curr_odd.get_item())\
                             + '|' + str(curr_odd.get_priority()) + ' --> '
            else:
                order_odd += str(curr_odd.get_item())\
                             + '|' + str(curr_odd.get_priority()) + ' --> NONE'

            curr_odd = curr_odd.get_next()

        return order_even + '\n' + order_odd

    def extracthigh(self):
        """
        (WackyQueue) -> object
        The first item in the
        WackyQueue will be removed and
        returned
        REQ: WackyQueue must not be isempty
        """
        # initialize our current's and previous
        # items in both lists
        curr_even = self._head_even
        curr_odd = self._head_odd

        # take the first item of the queue
        first_item = curr_odd.get_item()

        # Base case 1:
        # where there is only 1 item in the queue
        # clear the list
        if not curr_even:
            self._head_odd = None
            self._head_even = None

        # Base case 2:
        # there are 2 item's
        # remove the first and
        # make the second into the first
        elif curr_even and not curr_odd.get_next():
            self._head_even = None
            self._head_odd = curr_even

        # let even list be 2n and odd 2n + 1
        # if an item is removed from the list
        # then 2n - 1 = 2n - 1 and 2n + 1 - 1 = 2n
        # this indicates the all element's in even is now in odd list
        # and all elements in odd is now in even's list
        else:
            nex_odd = curr_odd.get_next()
            self._head_odd = curr_even
            self._head_even = nex_odd

        return first_item

    def getoddlist(self):
        """
        (WackyQueue) -> WackyNode
        Return the head of the odd list of
        the WackyQueue
        REQ: must not be isempty
        """
        return self._head_odd

    def getevenlist(self):
        """
        (WackyQueue) -> WackyNode
        Returns the head of the even list in the
        WackyQueue
        REQ: must be at least two items in WackyQueue
        """
        return self._head_even

    def isempty(self):
        """
        (WackyQueue) -> bool
        A boolean indicating whether
        WackyQueue is empty or not
        """
        return not self._head_odd

    def negateall(self):
        """
        (WackyQueue) -> NoneType
        negates the priorities of the elements
        in the queue
        REQ: must not be isempty
        """
        # let list = [a,b,c,...,2n,2(n+1)]
        # where a,b,c are <obj> in linked list
        # and 2n and 2n+1 are
        # even and odd last element respectively
        # odd = [a,c,...,2n+1]
        # even = [b,...,2n]
        # once negated
        # list = [-2(n+1),-2n ,...,-c,-b,-a]
        # odd = [-2n,...,-b,-6]
        # even = [-2(n+1),-c,-a]
        # so just reverse each list separately
        # and swap their heads since the smallest <pri>
        # becomes the biggest integer

        # if there is one item in WackyNode
        # just negate its priority
        if self._head_odd and not self._head_even:
            self._head_odd.set_priority(-self._head_odd.get_priority())

        # more than one item in WackyNode
        else:
            curr = self._head_odd
            prev = None

            # negate the odd <pri>
            # reverse the odd list
            while curr:
                curr.set_priority(-curr.get_priority())
                nex = curr.get_next()
                curr.set_next(prev)
                prev = curr
                curr = nex

            # point the head of odd to the new head
            # which was the previous odd tail
            self._head_odd = prev

            curr = self._head_even
            prev = None

            # negate the even <pri>
            # reverse the even list
            while curr:
                curr.set_priority(-curr.get_priority())
                nex = curr.get_next()
                curr.set_next(prev)
                prev = curr
                curr = nex

            # point the head of even to the new head
            # which was the previous even tail
            self._head_even = prev

            curr_even = self._head_even
            curr_odd = self._head_odd

            # swap the two list's
            self._head_even = None
            self._head_odd = None
            self._head_even = curr_odd
            self._head_odd = curr_even

    def insert(self, obj, pri):
        """
        (WackyQueue, int) -> NoneType
        Insert the object with priorities
        into the WackyQueue
        """
        curr = WackyNode(obj, pri)
        # CASE 1:
        # WackyQueue is empty
        if self.isempty():
            self._head_odd = curr

        # CASE 2:
        # There DNE head of even and
        # curr <pri> is <= head of odds <pri>
        elif not self._head_even and \
                self._head_odd.get_priority() >= curr.get_priority():

            self._head_even = curr
        # There DNE head of even and
        # curr <pri> is > head of odd
        elif not self._head_even and \
                self._head_odd.get_priority() < curr.get_priority():

            self._head_even = self._head_odd
            self._head_odd = curr

        # CASE 3:
        # if curr <pri> > head of odd <pri>
        # set head of odd to curr
        # head of even is the next of head of odd
        # head of odd is the new head of even
        elif curr.get_priority() > self._head_odd.get_priority():
            curr_odd = self._head_odd
            curr_even = self._head_even
            self._head_odd = curr
            self._head_even = curr_odd
            self._head_odd.set_next(curr_even)

        # CASE4:
        # if curr<pri> <= head of odd<pri> and curr <pri> > head of even
        # curr will be the new head of even and
        # next odd will be the previous head of even
        elif self._head_odd.get_priority() \
                >= curr.get_priority() > self._head_even.get_priority():

            # initialize our nodes
            prev_even = self._head_even
            curr_even = prev_even.get_next()
            prev_odd = self._head_odd
            curr_odd = prev_odd.get_next()

            # if there is one item in both list's
            # swap curr with even then set the previous
            # even item to the odd list
            if not curr_odd and not curr_even:
                self._head_even = curr
                prev_odd.set_next(prev_even)

            # if there is more than one item
            # in one or both list's
            else:
                self._head_even = curr
                prev_odd.set_next(prev_even)
                self._head_even.set_next(curr_odd)

        else:
            # CASE 5:
            # In the loop, check for
            # parallel(even and odd list has same # of elements)
            # first and then check for
            # adjacent(odd list has 1 more element than even)
            # current node that is need to be inserted = curr
            # using curr_of_odd and curr_of_even
            curr_even = self._head_even
            curr_odd = self._head_odd

            prev_even = None
            prev_odd = None
            adj = True

            while curr_even:
                # if  current_odd <pri> >= curr <pri> > curr_even <pri>
                # then swap the curr with current even
                # and swap nodes after the odd
                # with current even and make them the next evens
                if curr_odd.get_priority() >= \
                        curr.get_priority() > curr_even.get_priority():

                    # if parallel(even and odd has same number of items)
                    # make curr(new node) the current even
                    # and the next even is the next odd
                    if not curr_odd.get_next():
                        prev_even.set_next(None)
                        prev_even.set_next(curr)
                        nex_odd = curr_odd.get_next()
                        curr_odd.set_next(None)
                        curr_odd.set_next(curr_even)
                        curr_even.set_next(nex_odd)

                    # if adjacent(odd has one more element)
                    # make curr(new node) the current even and the next
                    # odd the current even and the next even the next odd
                    else:
                        nex_odd = curr_odd.get_next()
                        prev_even.set_next(None)
                        prev_even.set_next(curr)
                        curr_odd.set_next(None)
                        curr_odd.set_next(curr_even)
                        curr_even = curr
                        curr_even.set_next(nex_odd)

                    curr_even = None

                # if curr<pri> <= curr_even.<pri> > curr_odd.get_next()<pri>
                # curr will be swapped with current_odd
                # then current_odd will be the next current even
                # the nodes after current even will be the next of curr
                elif curr_odd.get_next() and \
                        curr_even.get_priority() >= curr.get_priority()\
                        > curr_odd.get_next().get_priority():

                    prev_odd = curr_odd
                    curr_odd = curr_odd.get_next()
                    prev_even = curr_even
                    curr_even = curr_even.get_next()
                    prev_even.set_next(None)
                    prev_even.set_next(curr_odd)
                    prev_odd.set_next(None)
                    prev_odd.set_next(curr)
                    curr_odd = curr
                    curr_odd.set_next(curr_even)
                    adj = False
                    curr_even = None

                else:
                    # traverse through the list's
                    prev_even = curr_even
                    curr_even = curr_even.get_next()
                    prev_odd = curr_odd
                    curr_odd = curr_odd.get_next()

            # Case 6
            # when out of the loop, check if
            # curr_of_odd and curr_of even are both
            # none at the same time
            # if their not then curr_odd has one
            # more element in
            # the list
            # If didn't insert a
            # node prior, insert it according to it
            if prev_even and not curr_odd:

                if curr.get_priority() <= prev_even.get_priority():
                    prev_odd.set_next(curr)

            else:
                # iff is adjacent and pri <= previous odd <pri>
                if adj and curr.get_priority() <= prev_odd.get_priority():
                    prev_even.set_next(curr)

    def changepriority(self, obj, pri):
        """
        (WackyQueue, object, int) -> NoneType
        changes the <pri> of the <obj> in the
        WackyQueue if it exist.
        """
        # target is the <obj>
        # we are trying to mutate
        target = None
        # CASE 0:
        # list is empty
        if self.isempty():
            target = None

        else:
            tail_odd = None
            # CASE 1:
            # if 1 item in WackyQueue and <pri> differs
            # change the <pri>
            if not self._head_even and self._head_odd.get_item() is obj and \
                    self._head_odd.get_priority() != pri:
                self._head_odd.set_priority(pri)
            # CASE 2:
            # there are two items in WackyQueue
            elif self._head_even and not self._head_odd.get_next():

                # target is head of even and <pri> differs
                # delete head of even and insert target to reorder
                if obj is self._head_even.get_item() and \
                                self._head_even.get_priority() != pri:

                    target = self._head_even.get_item()
                    self._head_even = None

                # target is head of odd and <pri> differs
                # delete head of odd and insert it later
                # head of even is our new head of odd
                elif obj is self._head_odd.get_item() and \
                        self._head_odd.get_priority() != pri:

                    target = self._head_odd.get_item()
                    self._head_odd = None
                    self._head_odd = self._head_even
                    self._head_even = None

                else:
                    # <obj> DNE in WackyQueue
                    target = None
            else:
                curr_odd = self._head_odd
                curr_even = self._head_even

                prev_odd = None
                prev_even = None
                # CASE 3:
                # traverse through both even and odd list
                # and find the object with that priority
                # once object is found set the previous node
                # of the same object to next and the next node
                # of the same object to the previous node
                # if target <pri> !=  <pri> then proceed
                # then use our insert method and insert the object
                # self.insert(object.get_item(), object.get_priority())
                # else don't mutate list

                while curr_even and curr_odd:
                    # CASE 0 (ODD CASES):
                    # <obj> is on the odd list
                    if curr_odd.get_item() == obj and\
                                    curr_odd.get_priority() != pri:
                        # <obj> is found delete it from the WackyQueue and
                        # insert it later
                        target = curr_odd.get_item()

                        # CASE 0(ODD)
                        # there are more than 3 elements in WackyQueue
                        # <obj> is the head of odd
                        # delete head of odd to insert it later
                        # current even is the new head of odd
                        # next odds are the head of even
                        if curr_odd is self._head_odd and\
                                self._head_odd.get_next():

                            nex_odd = self._head_odd.get_next()
                            curr_even = self._head_even
                            self._head_odd = None
                            self._head_even = None
                            self._head_odd = curr_even
                            self._head_even = nex_odd

                        # CASE 1(ODD):
                        # odd and even have equal # elements
                        # delete curr odd and make
                        # current even the next element
                        elif not curr_odd.get_next():
                            prev_even.set_next(None)
                            prev_odd.set_next(curr_even)

                        # CASE 3(ODD):
                        # odd list has 1 more element
                        # If the both list are same size:
                        # delete the current odd and and even
                        # make the current even the next odd
                        else:
                            nex_odd = curr_odd.get_next()
                            prev_even.set_next(None)
                            curr_odd.set_next(None)
                            prev_even.set_next(nex_odd)
                            prev_odd.set_next(curr_even)

                        # break loop
                        curr_odd = None

                    # CASE 1:
                    # three items in the list
                    # <obj> is the third item in WackyQueue
                    # delete the third item insert later
                    elif obj is self._head_odd.get_next().get_item() and \
                            self._head_odd.get_next().get_priority()\
                            != pri and not self._head_even.get_next():
                        target = self._head_odd.get_item()
                        self._head_odd.set_next(None)
                        curr_odd = None

                    # CASE 2(EVEN CASES):
                    # <obj> is on the even list
                    elif obj is curr_even.get_item() and\
                            curr_even.get_priority() != pri:

                        # <obj> is found, delete it and insert it later
                        target = curr_even.get_item()

                        # CASE 0(EVEN):
                        # 3 items in WackyQueue
                        # <obj> is the head of even
                        # delete the head of even insert it later
                        # head of odd is the new head of even
                        if obj is self._head_even.get_item() and \
                                not self._head_even.get_next()\
                                and self._head_odd.get_next():

                            self._head_even = None
                            self._head_even = self._head_odd.get_next()
                            self._head_odd.set_next(None)

                        # CASE 1(EVEN):
                        # odd and even have equal # elements
                        elif curr_odd.get_next():
                            # SPECIAL CASE:
                            # <obj> is the even head
                            # delete the head of even to
                            # insert it later head of odd is
                            # the new head of even
                            # what ever is after current even is the
                            # next of head of odd
                            if obj is self._head_even.get_item():
                                nex_even = curr_even.get_next()
                                self._head_even = None
                                self._head_even = self._head_odd.get_next()
                                self._head_odd.set_next(None)
                                self._head_odd.set_next(nex_even)
                            # GENERAL CASE:
                            # delete previous even and current odd
                            # next odd is the new current even
                            # and next even is the current odd
                            else:
                                nex_even = curr_even.get_next()
                                nex_odd = curr_odd.get_next()
                                prev_even.set_next(None)
                                prev_even.set_next(nex_odd)
                                curr_odd.set_next(None)
                                curr_odd.set_next(nex_even)

                        # break the loop
                        curr_even = None

                    # CASE 3(GENERAL ODD CASE):
                    # odd and even have equal # elements
                    elif not curr_odd.get_next() and\
                            curr_odd.get_item() is obj:
                        # <obj> is found delete from the list
                        # delete current odd
                        # delete current even
                        # current even is the new
                        # current odd
                        target = curr_odd.get_item()
                        prev_odd.set_next(None)
                        prev_even.set_next(None)
                        prev_odd.set_next(curr_even)
                        # break the loop
                        curr_even = None

                    # traverse through both even
                    # and odd list
                    else:
                        prev_odd = curr_odd
                        curr_odd = curr_odd.get_next()
                        prev_even = curr_even
                        curr_even = curr_even.get_next()
                        prev_tail_even = curr_even
                        tail_odd = curr_odd

                # prev_odd.set_next(None)
            # insert the target <obj> if
            # <obj> was found in either list's
            if target:
                self.insert(target, pri)
            # prev_tail_even.set_next(None)

if __name__ == '__main__':
    my_queue = WackyQueue()
    print("check_lists____test_case_1____\n")
    my_queue.insert('A', 10)
    my_queue.negateall()
    print()
    print(my_queue)
    my_queue.insert('B', 8)
    my_queue.negateall()
    print()
    print(my_queue)
    my_queue.insert('C', 8)
    my_queue.insert('C', 12)
    my_queue.insert('D', 8.5)
    my_queue.insert('E', 11)
    my_queue.insert('E', 11.23)
    my_queue.insert('E', 9.23)
    my_queue.insert('C', 8.2)
    my_queue.insert('C', 8.3)
    my_queue.insert('H', 7)
    my_queue.insert('H', 9)
    print(my_queue)
    print("\n____test_case_isempty____\n")
    empty_queue = WackyQueue()
    print('Expected: False\t\tGot: ' + str(my_queue.isempty()))
    print('Expected: True\t\tGot: ' + str(empty_queue.isempty()))
    print("\nChanged_PRIORITY\n")
    my_queue.changepriority('B', 11)
    my_queue.changepriority('H', 11)
    print(my_queue)
    print("\n____NEGATE_ALL___\n")
    my_queue.negateall()
    print(my_queue)
    print("\n____EXTRACT_HIGH___\n")
    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))

    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))

    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))

    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))

    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))
    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))
    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))
    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))
    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))
    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))
    print("Removed: " + str(my_queue.extracthigh()))
    print(my_queue)
    print("is_empty:\t" + str(my_queue.isempty()))
    print("Removed: " + str(my_queue.extracthigh()))
    print("is_empty:\t" + str(my_queue.isempty()))
    print("\ncheck_lists____test_case_2____\n")
    my_queue = WackyQueue()
    my_queue.insert('A', 100)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'A'> to pri<8>\n")
    my_queue.changepriority('A', 8)
    print(my_queue)
    print("\nInsert_obj<'B'>_pri<90>")
    my_queue.insert('B', 90)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'C'> to pri<100>\n")
    my_queue.changepriority('C', 8)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'B'> to pri<20>\n")
    my_queue.changepriority('B', 20)
    print(my_queue)
    print("\nInsert_obj<'L'>_pri<30>")
    my_queue.insert('L', 30)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'rand'> to pri<200>\n")
    my_queue.changepriority('rand', 200)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'B'> to pri<35>\n")
    my_queue.changepriority('B', 35)
    print(my_queue)
    print("\nInsert_obj<'D'>_pri<100.01>")
    my_queue.insert('D', 100.01)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'D'> to pri<-2>\n")
    my_queue.changepriority('D', -2)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'L'> to pri<-3>\n")
    my_queue.changepriority('L', -3)
    print(my_queue)
    print("\nInsert_obj<'H'>_pri<1>")
    my_queue.insert('H', 1)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'H'> to pri<-5>\n")
    my_queue.changepriority('H', -5)
    print(my_queue)
    print("\nInsert_obj<'N'>_pri<36>")
    my_queue.insert('N', 36)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'N'> to pri<-1>\n")
    my_queue.changepriority('p', 100000)
    my_queue.changepriority('N', -1)
    print(my_queue)
    print("\nInsert_obj<'O'>_pri<-40>")
    my_queue.insert('O', -40)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'H'> to pri<40>\n")
    my_queue.changepriority('H', 40)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'A'> to pri<0>\n")
    my_queue.changepriority('A', 0)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'D'> to pri<-20>\n")
    my_queue.changepriority('D', -20)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'N'> to pri<-40>\n")
    my_queue.changepriority('N', -40)
    print(my_queue)
    print("\nChanged_PRIORITY obj<'0'> to pri<4>\n")
    my_queue.changepriority('q', 4)
    my_queue.changepriority('O', 4)
    print(my_queue)
    print("\n____NEGATE_ALL___\n")
    my_queue.negateall()
    print(my_queue)
    while not my_queue.isempty():
        x = my_queue.extracthigh()
        print("REMOVED:\t" + str(x) +
              " \tISEMPTY:\t" + str(my_queue.isempty()))
    print("Look at the queue")
    print(my_queue)
    print("\ncheck_lists____test_case_2____\n")
    my_queue2 = WackyQueue()
    my_queue2.insert('A', 11)
    my_queue2.insert('A', 9)
    my_queue2.insert('A', 8)
    my_queue2.insert('A', 5)
    my_queue2.insert('A', 6)
    my_queue2.insert('A', 5)
    my_queue2.insert('A', 13)
    my_queue2.insert('A', 12)
    my_queue2.insert('A', 10)
    my_queue2.insert('A', 0)
    print(my_queue2)
    print("\n____extract_high_test_1____\n")
    my_queue3 = WackyQueue()
    my_queue3.insert('A', 5)
    my_queue3.insert('B', 4)
    my_queue3.insert('C', 3)
    my_queue3.insert('D', 2)
    print(my_queue3)
    print("REMOVED_ITEM:\t" + str(my_queue3.extracthigh()))
    print(my_queue3)
    print("REMOVED_ITEM:\t" + str(my_queue3.extracthigh()))

    print("QUEUE_IS_EMPTY:\t" + str(my_queue3.isempty()))
    print("\n____negate_test_1____\n")
    my_queue4 = WackyQueue()
    my_queue4.insert('A', 4)
    my_queue4.insert('B', 3)
    my_queue4.insert('C', 2)
    my_queue4.insert('D', 1)
    print(my_queue4)
    my_queue4.negateall()
    print("___________NEGATE_ALL__________")
    print(str(my_queue4) + '\n')
    print(str(my_queue) + '\n')
    my_queue.negateall()
    print(my_queue)
    my_queue = WackyQueue()
    for i in range(6):
        for j in 'ABCD':
            my_queue.insert(j, i)
    print(my_queue)
    for i in range(30):
        for j in "ABCD":
            my_queue.changepriority(j, i)
    print()
    # my_queue.changepriority('A', -1)
    # my_queue.changepriority('C', -1)
    # my_queue.changepriority('B', -1)
    # my_queue.changepriority('A', 100)
    # my_queue.changepriority('D', 200)
    # my_queue.changepriority('LD', 200)
    my_queue.insert('L', -2)
    # my_queue.insert('DD', -2)
    my_queue.changepriority('L', 200)
    # my_queue.negateall()
    print(my_queue)
