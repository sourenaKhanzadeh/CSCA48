"""
# Copyright Nick Cheng, 2016, 2018
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 2, CSCA48, Winter 2018
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

# Do not change any of the declarations of FormulaTree class and its
# subclasses!  This module provides the various FormulaTree subclasses
# you need to complete formula_game_functions.py


class FormulaTree:
    """Root of a formula tree."""
    def __init__(self: 'FormulaTree', symbol: str, children: list) -> None:
        """Create a FormulaTree with formula <symbol>, subtrees <children>.

        So far, symbol must be "-", "+", "*", or a lower case letter.

        >>> print(FormulaTree("x", []))
        FormulaTree('x', [])
        >>> print(FormulaTree("y", []))
        FormulaTree('y', [])
        """
        self._symbol, self._children = symbol, children[:]

    def __repr__(self: 'FormulaTree') -> str:
        """Return string representation of FormulaTree self."""
        return 'FormulaTree({}, {})'.format(
            repr(self._symbol), repr(self._children))

    def __eq__(self: 'FormulaTree', other: object) -> bool:
        """Return whether FormulaTree self is equivalent to other

        >>> FormulaTree("x", []).__eq__(FormulaTree("y", []))
        False
        >>> FormulaTree("y", []).__eq__(FormulaTree("y", []))
        True
        """
        return (isinstance(other, FormulaTree) and
                self._symbol == other._symbol and
                self._children == other._children)

    def get_symbol(self: 'FormulaTree') -> str:
        """Return the symbol at the root of the FormulaTree self.

        >>> FormulaTree("x", []).get_symbol()
        'x'
        >>> FormulaTree("#", []).get_symbol()
        '#'
        """
        return self._symbol

    def get_children(self: 'FormulaTree') -> list:
        """Return the children of the root of the FormulaTree self.

        >>> FormulaTree("x", []).get_children()
        []
        >>> FormulaTree("x", [FormulaTree("y", [])]).get_children()
        [FormulaTree('y', [])]
        """
        return self._children[:]

    def set_children(self: 'FormulaTree', children: list) -> None:
        """Set children of the root of the FormulaTree self to <children>.

        >>> ft = FormulaTree("x", [])
        >>> ft.set_children([FormulaTree("y", [])])
        >>> ft.get_children()
        [FormulaTree('y', [])]
        """
        self._children = children[:]


class Leaf(FormulaTree):
    """FormulaTree with lower case letter symbol and no children."""
    def __init__(self: 'Leaf', symbol: str) -> None:
        """Create a Leaf with symbol and no children."""
        FormulaTree.__init__(self, symbol, [])

    def __repr__(self: 'Leaf') -> str:
        """Return string representation of Leaf self."""
        return 'Leaf({})'.format(repr(self._symbol))


class UnaryTree(FormulaTree):
    """FormulaTree with a single child.
    So far, it's used only for NOT nodes.
    """
    def __init__(self: 'UnaryTree', symbol: str,
                 child: 'FormulaTree') -> None:
        """Create a UnaryTree with formula symbol and (only) child."""
        FormulaTree.__init__(self, symbol, [child])

    def __repr__(self: 'UnaryTree') -> str:
        """Return string representation of UnaryTree self."""
        return 'UnaryTree({}, {})'.format(
            repr(self._symbol), repr(self._children[0]))


class BinaryTree(FormulaTree):
    """FormulaTree with two children.
    So far, it's only used for AND and OR nodes.
    """
    def __init__(self: 'BinaryTree', symbol: str,
                 left: 'FormulaTree', right: 'FormulaTree') -> None:
        """Create a BinaryTree with formula symbol, and left and right
        children.
        """
        FormulaTree.__init__(self, symbol, [left, right])

    def __repr__(self: 'BinaryTree') -> str:
        """Return string representation of BinaryTree self."""
        return 'BinaryTree({}, {}, {})'.format(repr(self._symbol),
                                               repr(self._children[0]),
                                               repr(self._children[1]))


class NotTree(UnaryTree):
    """A UnaryTree rooted at a NOT ("-") node.

    >>> ftx = Leaf("x")
    >>> fty = Leaf("y")
    >>> ftand = AndTree(fty, fty)
    >>> ftor = OrTree(ftx, ftand)
    >>> NotTree(ftor).__eq__(\
NotTree(OrTree(Leaf('x'), AndTree(Leaf('y'), Leaf('y')))))
    True
    """
    def __init__(self: 'NotTree', child: 'FormulaTree') -> None:
        """Creat a NotTree with (only) child"""
        UnaryTree.__init__(self, '-', child)

    def __repr__(self: 'NotTree') -> str:
        """Return string representation of NotTree self."""
        return 'NotTree({})'.format(repr(self._children[0]))


class OrTree(BinaryTree):
    """A BinaryTree rooted at an OR ("+") node.

    >>> ftx = Leaf("x")
    >>> fty = Leaf("y")
    >>> OrTree(ftx, fty) == OrTree(Leaf('x'), Leaf('y'))
    True
    """

    def __init__(self: 'OrTree', left: 'FormulaTree',
                 right: 'FormulaTree') -> None:
        BinaryTree.__init__(self, "+", left, right)

    def __repr__(self: 'OrTree') -> str:
        """Return string representation of OrTree self."""
        return 'OrTree({}, {})'.format(repr(self._children[0]),
                                       repr(self._children[1]))


class AndTree(BinaryTree):
    """BinaryTree rooted at an AND ('.') node."""
    def __init__(self: 'AndTree', left: 'FormulaTree',
                 right: 'FormulaTree') -> None:
        """New DotTree with left and right children

        >>> ftx = Leaf("x")
        >>> fty = Leaf("y")
        >>> AndTree(ftx, fty) == AndTree(Leaf('x'), Leaf('y'))
        True
        """
        BinaryTree.__init__(self, "*", left, right)

    def __repr__(self: 'AndTree') -> str:
        """Return string representation of AndTree self."""
        return 'AndTree({}, {})'.format(repr(self._children[0]),
                                        repr(self._children[1]))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    f = FormulaTree('x', [])
    f.set_children([FormulaTree('y', [])])
    f.get_children()[0].set_children([FormulaTree('z', [])])
    l = Leaf('+')
    print(repr(l))
    print(repr(f))

# def build_tree(formula: str):
#     '''
#     (str) -> FormulaTree or NoneType
#     checks if the
#     formula is valid
#     if valid then returns the formula
#     else it will not return anything
#     REQ: formula must not be empty
#     '''
#     sign = {'+', '-', '*'}
#     num_open_bracket = 0
#     num_closed_bracket = 0
#     # We are trying to find cases
#     # that makes our formula invalid
#     # if so valid = None
#
#     # CASE 0:
#     # no formula is given
#     # then it is not valid
#     if len(formula) == 0:
#
#         valid = None
#     # CASE1:
#     # formula has 1 letter
#     # then it must be a lower case letter(variable)
#     elif len(formula) == 1:
#         if formula.islower():
#             valid = FormulaTree(formula, [])
#         else:
#             valid = None
#     # CASE 2:
#     # formula starts with -
#     elif formula[0] == '-':
#         # if there is nothing after -
#         # then invalid formula
#         if len(formula) == 1:
#             valid = None
#         # if after - is a variable then make the root
#         # and continue the formula
#         elif formula[1].islower():
#
#             valid = NotTree(formula[1])
#         # if a parenthesis is after a - then
#         # the next letter must be a variable
#         # and no closed ) after it
#         elif len(formula) > 3 and \
#                         formula[1] == '(' and \
#                 formula[2].islower() and \
#                         formula[3] != ')':
#
#             # continue the formula
#             formula = formula[1:]
#
#         else:
#             valid = None
#     # CASE GENERAL:
#     else:
#         prev = None
#         # as long as formula is not empty
#         while formula != '':
#             if formula[0] == '-':
#                 # if there is nothing after -
#                 # then invalid formula
#                 if len(formula) == 1:
#                     valid = None
#                 # if after - is a variable then make the root
#                 # and continue the formula
#                 elif formula[1].islower():
#
#                     valid = NotTree(formula[1])
#                 # if a parenthesis is after a - then
#                 # the next letter must be a variable
#                 # and no closed ) after it
#                 elif len(formula) > 3 and \
#                                 formula[1] == '(' and \
#                         formula[2].islower() and \
#                                 formula[3] != ')':
#
#                     # continue the formula
#                     formula = formula[1:]
#
#                 else:
#                     valid = None
#
#             elif formula[0] in sign:
#                 if len(formula) == 1:
#                     valid = None
#
#             elif formula[0] == '(':
#                 if len(formula) == 1:
#                     valid = None
#                 elif formula[1] == '-' or formula[1].islower():
#                     formula = formula[1:]
#                     num_open_bracket += 1
#                 else:
#                     valid = None
#
#             elif formula[0].islower():
#                 formula = formula[1:]
#
#             elif formula[0] == ')':
#                 if len(formula) == 1:
#                     formula = ''
#                     num_closed_bracket += 1
#                 elif formula[1] in sign:
#                     formula = formula[1]
#                     num_closed_bracket += 1
#                 else:
#                     valid = None
#
#             else:
#                 valid = None
#
#             prev = formula[0]
#
#     if num_closed_bracket == num_open_bracket:
#         return valid
# ^--- build_tree back up here
