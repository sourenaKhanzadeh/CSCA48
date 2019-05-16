"""
# Copyright Nick Cheng, 2018
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


# You will not be submitting this file.
# So make changes only for your own testing purposes.

class WackyNode:
    """A node for linked lists in a WackyQueue."""

    def __init__(self: 'WackyNode',
                 item: object, priority: int) -> None:
        self._next = None
        self._item = item
        self._priority = priority

    def get_next(self: 'WackyNode') -> object:
        return self._next

    def set_next(self: 'WackyNode', next: 'WackyNode') -> None:
        self._next = next

    def get_item(self: 'WackyNode') -> object:
        return self._item

    def set_item(self: 'WackyNode', item: object) -> None:
        self._item = item

    def get_priority(self: 'WackyNode') -> int:
        return self._priority

    def set_priority(self: 'WackyNode', priority: int) -> None:
        self._priority = priority

# # ODD CASES if <obj> is in odd list
# # CASE 1:
# # 1 item in WackyQueue
# # remove the item
# if self._head_odd.get_item() == obj and \
#                 self._head_odd.get_priority() != pri:
#
#     target = self._head_odd.get_item()
#
#     self._head_odd = None
# # CASE 2:
# # 3 items in WackyQueue
# # remove head and swap even and nex_odd
# elif not self._head_odd.get_next() and \
#                 self._head_odd.get_item() == obj and \
#                 self._head_odd.get_priority() != pri:
#     target = self._head_odd.get_item()
#
#     self._head_odd = self._head_even
#     self._head_even = None
#
# # CASE 3
# # more than three items
# # in WackyQueue and <obj> is head of odd
# # remove head swap even and odd
# elif self._head_odd.get_item() == obj and \
#                 self._head_odd.get_priority() != pri:
#
#     target = self._head_odd.get_item()
#
#     nex_odd = self._head_odd.get_next()
#     self._head_odd = self._head_even
#     self._head_even = nex_odd
# # EVEN CASES if <obj> is in even list
# # CASE 1:
# # 2 item's in WackyQueue
# # just remove even head
# elif not self._head_odd.get_next() and \
#                 self._head_even.get_item() == obj and \
#                 self._head_even.get_priority() != pri:
#     target = self._head_even.get_item()
#     self._head_even = None
#
# # CASE 3:
# # more than 4 items in WackyQueue
# # take out even head and swap
# # even and odd list
# elif not self._head_even and self._head_odd.get_item() != obj:
#     target = None
# elif self._head_even.get_next() and \
#                 self._head_even.get_item() == obj and \
#                 self._head_even.get_priority() != pri:
#     target = self._head_even.get_item()
#
#     nex_even = self._head_even.get_next()
#     nex_odd = self._head_odd.get_next()
#     self._head_odd.set_next(None)
#     self._head_even = None
#     self._head_even = nex_odd
#     self._head_odd.set_next(nex_even)
# # CASE 4:
# # 3 items in WackyQueue
# # take head of even set the
# # next odd and
# elif self._head_even.get_item() == obj and \
#                 self._head_even.get_priority() != pri:
#     target = self._head_even.get_item()
#
#     nex_odd = self._head_odd.get_next()
#     self._head_odd.set_next(None)
#     self._head_even = None
#     self._head_even = nex_odd
#
# else:
#     # if there is an obj then curr odd must
#     # exist
#     while curr_odd and curr_even:
#
#         # CASE 4 (ODD'S):
#         # then our current odd is our target
#         # node to mutate
#         if curr_odd.get_item() == obj and \
#                         curr_odd.get_priority() != pri:
#             target = curr_odd.get_item()
#             # if next_odd exist
#             # then set the previous
#             # odd to the next odd
#
#             # CASE 1:
#             # There is an element after
#             # target, set the next_even
#             # to the previous odd element
#             # and the next odd to the
#             # current even
#             if curr_even.get_next():
#
#                 nex_odd = curr_odd.get_next()
#                 prev_odd.set_next(None)
#                 prev_odd.set_next(curr_even)
#                 prev_even.set_next(None)
#                 prev_even.set_next(nex_odd)
#
#             # CASE 2:
#             # there is no element after
#             # our current even, set the
#             # next odd to None
#             else:
#                 prev_odd.set_next(None)
#                 prev_even.set_next(None)
#                 prev_odd.set_next(curr_even)
#
#             curr_odd = None
#         # CASE 5 (EVEN'S)
#         # if our <obj> is in the even list
#         # then our current even is our target
#         # node to mutate
#         elif curr_even.get_item() == obj and \
#                         curr_even.get_priority() != pri:
#             # target found
#             target = curr_even.get_item()
#
#             # CASE 1:
#             # There is an element after
#             # target, set the next_odd
#             # to the previous even element
#             # and the next even to the
#             # current odd
#             if curr_even.get_next():
#
#                 nex_even = curr_even.get_next()
#                 nex_odd = curr_odd.get_next()
#                 prev_even.set_next(None)
#                 prev_even.set_next(nex_odd)
#                 curr_odd.set_next(None)
#                 curr_odd.set_next(nex_even)
#
#             # CASE 2:
#             # there is no element after
#             # our current even, set the
#             # previous even to the next odd
#             # and current odd to None
#             else:
#                 # nex_odd = curr_odd.get_next()
#                 # curr_odd.set_next(None)
#                 # prev_even.set_next(None)
#                 prev_even.set_next(curr_odd.get_next())
#                 prev_odd.get_next().set_next(None)
#             curr_odd = None
#
#         # traverse through the list
#         else:
#             prev_even = curr_even
#             prev_odd = curr_odd
#             curr_odd = curr_odd.get_next()
#             curr_even = curr_even.get_next()


#  target = None
#         obj_exist = False
#
#         # CASE 0:
#         # list is empty
#         if self.isempty():
#             target = None
#
#         else:
#             # CASE 1:
#             if not self._head_even and self._head_odd.get_item() is obj and \
#                    self._head_odd.get_priority() != pri:
#                     self._head_odd.set_priority(pri)
#             # CASE 2:
#             elif self._head_even and not self._head_odd.get_next():
#
#                 if obj is self._head_even.get_item() and self._head_even.get_priority() != pri:
#                     target = self._head_even.get_item()
#                     self._head_even = None
#
#                 elif obj is self._head_odd.get_item() and self._head_odd.get_priority() != pri:
#                     target = self._head_odd.get_item()
#                     self._head_odd = None
#                     self._head_odd = self._head_even
#                     self._head_even = None
#
#                 else:
#                     target = None
#             # CASE 3:
#             else:
#                 curr_odd = self._head_odd
#                 curr = self._head_odd
#                 curr_even = self._head_even
#
#                 prev_odd = None
#                 prev_even = None
#                 # traverse through both even and odd list
#                 # and find the object with that priority
#                 # once object is found set the previous node
#                 # of the same object to next and the next node
#                 # of the same object to the previous node
#                 # if target <pri> !=  <pri> then proceed
#                 # then use our insert method and insert the object
#                 # self.insert(object.get_item(), object.get_priority())
#                 # else don't mutate list
#
#                 while curr and curr_even:
#                     # find if the <obj> exist's in
#                     # both even and odd list
#                     if curr_odd.get_item() == obj:
#                         target = curr_odd.get_item()
#                         obj_exist = True
#                         curr = None
#
#                     elif curr_even and curr_even.get_item() == obj:
#                         target = curr_even.get_item()
#                         obj_exist = True
#                         curr = None
#                     else:
#                         # traverse through the both even
#                         # and odd list
#                         prev_odd = curr_odd
#                         curr_odd = curr_odd.get_next()
#                         prev_even = curr_even
#                         curr_even = curr_even.get_next()
#
#                 # <obj> exist
#                 if obj_exist:
#                     # CASE ODD:
#                     # if <obj> in odd list and has a different <pri>
#                     if target is curr_odd.get_item() and curr_odd.get_priority() != pri:
#                         # CASE 1(ODD):
#                         # if <obj> is the head of more than 3 elements in odd list
#                         # delete head make even new odd head and next_odd the new
#                         # even head
#                         if curr_odd is self._head_odd and self._head_odd.get_next():
#
#                             nex_odd = self._head_odd.get_next()
#                             curr_even = self._head_even
#                             self._head_odd = None
#                             self._head_even = None
#                             self._head_odd = curr_even
#                             self._head_even = nex_odd
#                         # CASE 2(ODD):
#                         # odd and even have equal # elements
#                         # delete curr odd and make current even the next element
#                         elif not curr_odd.get_next():
#                             curr_even_odd = None
#                             prev_even.set_next(None)
#                             prev_odd.set_next(curr_even)
#                         # CASE 3(ODD):
#                         # odd list has 1 more element
#                         # If the both list are same size:
#                         # delete the current odd and and even
#                         # make the current even the next odd
#                         else:
#                             nex_odd = curr_odd.get_next()
#                             prev_even.set_next(None)
#                             curr_odd.set_next(None)
#                             prev_even.set_next(nex_odd)
#                             prev_odd.set_next(curr_even)
#                     # CASE 0(EVEN):
#                     # if Two item's in the WackyQueue
#                     elif target is self._head_even.get_item() and self._head_even.get_priority() != pri and \
#                             not self._head_odd.get_next():
#
#                         self._head_even = None
#                     # CASE 1(EVEN)
#                     elif target is curr_even.get_item() and curr_even.get_priority() != pri:
#                         # CASE 2(EVEN)
#                         if curr_even is self._head_even and self._head_even.get_next():
#                             nex_odd = self._head_odd.get_next()
#                             nex_even = self._head_even.get_next()
#
#                             self._head_even = None
#                             self._head_odd.set_next(None)
#                             self._head_even = nex_odd
#                             self._head_odd.set_next(nex_even)
#
#                         # CASE 3(EVEN)
#                         elif curr_odd.get_next() and curr_even.get_next():
#                             nex_odd = curr_odd.get_next()
#                             nex_even = curr_even.get_next()
#                             curr_odd.set_next(None)
#                             prev_even.set_next(None)
#                             curr_even.set_next(None)
#                             prev_even.set_next(nex_odd)
#                             curr_odd.set_next(nex_even)
#
#                         # CASE 4(EVEN)
#                         elif curr_odd.get_next() and not curr_even.get_next():
#                             if prev_even is not curr_even:
#                                 while curr_even.get_item() is not obj:
#                                     prev_even = curr_even
#                                     curr_even = curr_even.get_next()
#
#                             elif prev_even.get_next() is curr_even:
#                                 nex_even = curr_even.get_next()
#                                 nex_odd = curr_odd.get_next()
#                                 curr_odd.set_next(None)
#                                 curr_odd.set_next(None)
#                                 prev_even.set_next(None)
#                                 curr_odd.set_next(nex_even)
#                                 prev_even.set_next(nex_odd)
#
#                         else:
#                             prev_even.set_next(None)
#                             prev_odd.set_next(None)
#                             prev_even.set_next(curr_odd)
#
#                     else:
#                         target = None
#
#                 else:
#                     target = None
#
#             # insert the target <obj> if
#             # target is not None
#             if target:
#                 self.insert(target, pri)

if __name__ == '__main__':
    import doctest

    doctest.testmod()
