"""
# Copyright Nick Cheng, 2016, 2018
# Copyright Sourena Khanzadeh, 2018
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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file. If not, see <http://www.gnu.org/licenses/>.
"""

from formula_tree import FormulaTree, Leaf, NotTree, AndTree, OrTree

invalid = False


def build_tree(formula):
    """
    (str) -> FormulaTree or NoneType
    checks if the
    formula is valid
    if valid then returns the formula
    else it will not return anything
    >>> build_tree('x')
    Leaf('x')
    >>> build_tree('-x')
    NotTree(Leaf('x'))
    >>> build_tree('(x+y)')
    OrTree(Leaf('x'), Leaf('y'))
    >>> build_tree('(x*y)')
    AndTree(Leaf('x'), Leaf('y'))
    >>> build_tree('x-')

    >>> build_tree('xy')

    """
    # if anywhere of our formula
    # makes invalid True just
    # stop the recursive call and
    # return None
    global invalid
    # CASE 0(SIMPLEST CASE):
    # formula is empty
    if len(formula) == 0:
        valid = None
    # CASE 1(formula is a variable)
    # second simplest case where
    # one variable
    elif len(formula) == 1 and formula.islower():
        valid = Leaf(formula)
    # CASE 2('-'):
    # an Unary NotTree
    # of whatever is build after
    elif len(formula) > 1 and formula[0] == '-':
        valid = NotTree(build_tree(formula[1:]))
    # CASE 3(GENERAL '('):
    # First the root must be found
    # then left and right child
    # taken to be build and surrounded
    # by OrTree()/AndTree() depending
    # on the operation symbol
    elif formula[0] == '(' == formula[1] == '(' and \
            formula.count('(') == formula.count(')'):

        sign_ind = formula.index(')')
        # first root
        sign_root = root_finder(formula, sign_ind) + 1
        # '*' -> AndTree(left_child,right_child)
        if formula[-1] == formula[-2] == ')' or formula[-2].islower():
            if formula[sign_root] == '*':
                valid = AndTree(build_tree(formula[1:sign_root]),
                                build_tree(formula[sign_root + 1:-1]))
            # '+' -> AndTree(left_child,right_child)
            elif formula[sign_root] == '+':

                valid = OrTree(build_tree(formula[1:sign_root]),
                               build_tree(formula[sign_root + 1:-1]))
            else:
                valid = None
                invalid = True
        else:
            valid = None
            invalid = True
    # CASE 4('(-'):
    # First the root must be found
    # then left and right child
    # taken to be build and surrounded
    # by OrTree()/AndTree() depending
    # on the operation symbol
    elif formula[0] == '(' and formula[1] == '-' and \
            formula.count('(') == formula.count(')') and \
            ('+' in formula or '*' in formula) and \
            (formula.count('+') > 1 or formula.count('*') > 1):
        sign_ind = formula.index(')')
        # first root
        sign_root = root_finder(formula, sign_ind) + 1
        # '*' -> AndTree(left_child,right_child)
        if formula[-1] == formula[-2] == ')' or formula[-2].islower():
            if formula[sign_root] == '*':
                valid = AndTree(build_tree(formula[1:sign_root]),
                                build_tree(formula[sign_root + 1:-1]))
            # '+' -> AndTree(left_child,right_child)
            elif formula[sign_root] == '+':

                valid = OrTree(build_tree(formula[1:sign_root]),
                               build_tree(formula[sign_root + 1:-1]))
            else:
                valid = None
                invalid = True
        else:
            valid = None
            invalid = True

    # CASE 5('('):
    # Binary operators '+' or '*'
    # * -> AndTree(left,right)
    # + -> OrTree(left,right)
    # build left and right child and
    # surrounded by AndTree\OrTree depending
    # on the operation sign
    # the formula in format F = '(' + f1 + '+' + f2 + ')'
    elif formula[0] == '(' and \
            formula[-1] == ')' and formula.count('(') == formula.count(')'):
        sign_ind = formula.index(')')
        # simplest binary filter that makes the OrTree()
        if '+' in formula and \
                formula.count('+') == 1 and \
                len(formula[sign_ind:]) == 1:

            if formula[formula.index('+') - 1].islower() \
                    and formula[-2].islower():
                valid = \
                    OrTree(build_tree(formula[1:]),
                           build_tree(formula
                           [formula.index('+') + 1:formula.index(')',
                            formula.index('+'))]))

            else:
                valid = None
                invalid = True

        # simplest binary filter that makes the AndTree()
        elif '*' in formula and \
                formula.count('*') == 1 and \
                len(formula[sign_ind:]) == 1:

            if formula[formula.index('*') - 1].islower() \
                    and formula[-2].islower():

                valid = \
                    AndTree(build_tree(formula[1:]),
                            build_tree(
                            formula[formula.index('*') + 1:
                                    formula.index(')')]))
            else:
                valid = None
                invalid = True

        # formula starts with a leaf after ('(') and has a '+' after
        elif '+' in formula and \
                formula.index('+') < formula.index(')'):
            # iff there is a variable before operator
            if formula[formula.index('+') - 1].islower():
                valid = OrTree(build_tree(formula[1:formula.index('+') + 1]),
                               build_tree(formula[formula.index('+') + 1:-1]))
            else:
                valid = None
                invalid = True

        # formula starts with a leaf after ('(') and has a '*' after
        elif '*' in formula and \
                formula.index('*') < formula.index(')'):
            # iff there is a variable before operator
            if formula[formula.index('*') - 1].islower():
                valid = AndTree(build_tree(formula[1:formula.index('*') + 1]),
                                build_tree(formula[formula.index('*') + 1:-1]))
            else:
                valid = None
                invalid = True
        else:
            valid = None
            invalid = True

    # CASE 4(GENERAL VARIABLE):
    # current is .lower therefore must
    # be a variable; must be a Leaf()
    elif formula[0].islower():
        valid = Leaf(formula[0])
        # check if - or another var is after variable and make it invalid
        if len(formula) > 1 and (formula[1] == '-' or formula[1].islower()):
            invalid = True
        else:
            invalid = False
    # Invalid
    else:

        valid = None
        invalid = True

    # return valid iff it is not invalid else return None
    return valid if not invalid else None


def root_finder(formula, sign_ind):
    """
    (str) -> int
    finds the main root
    of the binary operator
    '*' or '+'
    REQ: # of ( == )
    REQ: formula to be valid
    >>> root_finder('((x+y)*(n+q))', 5)
    5
    >>> root_finder('(((x+y)*(n+q))+(q+w))', 6)
    13
    """
    # count the # of ( and ) until the first sign
    open_par = formula[:sign_ind + 1].count('(')
    close_par = formula[:sign_ind + 1].count(')')
    # as long as the number of differences is not 1
    # slice and count the number of new parenthesis
    # and find the index of the root sign
    if close_par != open_par - 1:
        while close_par != -1:
            open_par = \
                formula[sign_ind + 1:formula.index(')',
                        sign_ind + 1)].count('(')

            close_par = \
                formula[sign_ind + 1:formula.index(')',
                        sign_ind + 1)].count(')')

            if close_par == open_par - 1:
                sign_ind = \
                    formula.index(')',
                                  formula.index(')', sign_ind + 1)) + 1
                close_par = -1
    # if sign is not the end as in
    # close bracket
    if len(formula[sign_ind:]) == 1:
        sign_ind = formula.index(')')

    return sign_ind


def draw_formula_tree(root):
    '''
    (FormulaTree) -> str
    takes the root of the
    formula tree and draws that tree
    REQ: root must be valid
    >>> x = build_tree('(((x+y)*(n+q))+(q+w))')
    >>> draw_formula_tree(x)
    '+ + w\\n    q\\n  * + q\\n      n\\n    + y\\n      x'
    >>> x = build_tree('(x+y)')
    >>> draw_formula_tree(x)
    '+ y\\n  x'
    '''
    # .replace('\n', '\n  ') is to align the tree correctly

    # CASE 0 (root not given):
    if root is None:
        res = ''
    # CASE 1 (root is '*'):
    # align the right and left children
    # inside of the '*' symbol
    elif root.get_symbol() == '*':
        # take the left and right child of root
        right = draw_formula_tree(root.get_children()[1])
        left = draw_formula_tree(root.get_children()[0])
        # align the left and right child
        align = right + '\n' + left
        res = '* ' + align.replace('\n', '\n  ')
    # CASE 2 (root is '+'):
    # align the right and left children
    # inside of the '+' symbol
    elif root.get_symbol() == '+':
        # take the left and right child of root
        right = draw_formula_tree(root.get_children()[1])
        left = draw_formula_tree(root.get_children()[0])
        # align the left and right child
        align = right + '\n' + left
        res = '+ ' + align.replace('\n', '\n  ')
    # CASE 3 (root is '-')
    # draw the child with one pre space
    elif root.get_symbol() == '-':
        res = '- ' + \
            draw_formula_tree(root.get_children()[0]).replace('\n', '\n  ')

    # CASE 4 (Second Simplest CASE):
    # root is a variable so only take
    # the string representation of that variable
    else:
        res = root.get_symbol()

    return res


def evaluate(root, variables, values):
    '''
    (FormulaTree, str, str) -> int
    evaluates the formula given
    and returns an integer indicating
    a boolean true or false
    REQ: existent variables must be inputted
    REQ: root must not be == None
    REQ: values must be either 0 or 1
    REQ: len(variables) == len(values)
    >>> x = build_tree('(((x+y)*(n+q))+(q+w))')
    >>> evaluate(x, 'xynqw', '001010')
    1
    >>> evaluate(x, 'xynqw', '000000')
    0
    '''

    # CASE 0 (root symbol is variable):
    # take the corresponding value
    # turn it into an integer
    if root.get_symbol().islower():
        index = variables.index(root.get_symbol())
        res = int(values[index])

    # CASE 1 (root symbol is '-' )
    # take the post variable's value of
    # it and negate it if value
    # 0 -> 1
    # 1 -> 0
    elif root.get_symbol() == '-':
        val = evaluate(root.get_children()[0], variables, values)

        res = 1 if val == 0 else 0

    # CASE 2 (root symbol is '*')
    # And symbol indicates is binary
    # take the value of left and right child
    # let left = l and right = r
    # l or r == 0 -> 0
    # l == r == 1 -> 1
    elif root.get_symbol() == '*':
        # take left and right childs values
        val_right = evaluate(root.get_children()[0], variables, values)
        val_left = evaluate(root.get_children()[1], variables, values)

        res = 1 if val_left == val_right == 1 else 0

    # CASE 3 (root symbol is '+')
    # And symbol indicates is binary
    # take the value of left and right child
    # let left = l and right = r
    # l or r == 1 -> 1
    # l == r == 0 -> 0
    elif root.get_symbol() == '+':
        # take left and right childs values
        val_right = evaluate(root.get_children()[0], variables, values)
        val_left = evaluate(root.get_children()[1], variables, values)

        res = 0 if val_left == val_right == 0 else 1

    return res


def play2win(root, turns, variables, values):
    '''
    (FormulaTree, str, str, str) -> int
    Takes in a Formula and the turns of the players
    and the variables and the values assigned to the
    variables to give the next best possible move
    to the next player. A wins if 0 is returned E wins
    if 1 is returned
    REQ: No more than Two players(A, E)
    REQ: len(values) < len(turns)
    REQ: FormulaTree != None
    REQ: existing variables
    REQ: len(turns) = len(variables)
    >>> x = build_tree('(((x+y)*(n+q))+(q+w))')
    >>> play2win(x, 'AEAAA', 'xynqw', '')
    0
    >>> play2win(x, 'AEAAA', 'xynqw', '1')
    1
    >>> play2win(x, 'AEAAA', 'xynqw', '11')
    0
    >>> play2win(x, 'AEAAA', 'xynqw', '110')
    0
    '''
    # Case 0:
    # all values been assigned but one;
    # choose the best possible move
    if len(values) == len(turns) - 1:

        best_move = last_best_win(root, turns, variables, values)

    # CASE 2 (len(values) <= len(turns) - 2)
    # this is the general case
    # since A wins if best_move = 0  and E wins if
    # best_move = 1 regardless of the And/Or
    # operators then the only factor is the number of('-')
    # that will determine whether the value must be other
    # than the default the whole purpose is to count the
    # relative number of ('-') and return the correct value
    else:
        # take the string representation of our
        # partitioned negation with our convention
        # * = the unique desired variable
        # + = common variable helped to count the number of ('-')
        # - = negations
        neg_part = partition_negations(root, variables, values)
        # make the unique var our last element
        neg_part = neg_part[:neg_part.index('*') + 1]
        # reverse it
        neg_part = neg_part[::-1]
        # length from unique to the bracket
        len_unique_bracket = len(neg_part[0:neg_part.index('(')]) \
            if '(' in neg_part else None
        # length from unique to the common iff '*' is after '+'
        # else len_unique_common DNE which is represented as -1
        len_unique_common = len(neg_part[0:neg_part.index('+')]) \
            if '+' in neg_part else -1
        # CASE 0 (No Common):
        # if len_unique_common DNE
        # then count every negation
        if len_unique_common == -1:
            neg_len = neg_part.count('-')
        # CASE 1():
        elif len_unique_bracket and len_unique_bracket < len_unique_common:
            neg_len = neg_part[0:neg_part.index('+')].count('-')
        # CASE 2(len(Common < len(bracket))):
        else:
            # CASE 2.1(No negation part of range(len(common)))):
            # This indicates the only negation count we need
            # is before the bracket
            if len_unique_bracket and len(neg_part) > 1 and neg_part[1] != '-':
                neg_len = neg_part[neg_part.index('('):].count('-')
            # CASE 2.2(Brackets DNE):
            # if bracket DNE then
            # count all ('-') up to common('+')
            elif len_unique_bracket is None:
                neg_len = neg_part[:neg_part.index('+')].count('-')
            # CASE 2.3(General Case)):
            # count all the ('-') in range(bracket and common)
            # then add them all up
            else:
                neg_len = neg_part[neg_part.index('('):].count('-')
                neg_len = neg_len + neg_part[:neg_part.index('+')].count('-')

        # Case 1(Player A's turn):
        # all ('-') is counted
        # let count('-') be m numbers
        # m is odd -> best_move = 1
        # m is even -> best_move = 0
        if turns[len(values)] == 'A':

            best_move = 0 if neg_len % 2 == 0 else 1
        # Case 2(Player E's turn):
        # all ('-') is counted
        # let count('-') be m numbers
        # m is even -> best_move = 1
        # m is odd -> best_move = 0
        else:

            best_move = 1 if neg_len % 2 == 0 else 0

    return best_move


def last_best_win(root, turns, variables, values):
    """
    (FormulaTree, str, str, str) -> int
    Used only for the last possible best
    move for the current player
    REQ: This works iff
    len(values) = len(turns) - 1
    REQ: No more than Two players(A, E)
    REQ: len(values) < len(turns)
    REQ: FormulaTree != None
    REQ: existing variables
    REQ: len(turns) = len(variables)
    >>> x = build_tree('(((x+y)*(n+q))+(q+w))')
    >>> last_best_win(x, 'AEAAA', 'xynqw', '1111')
    0
    >>> last_best_win(x, 'AEAAE', 'xynqw', '1111')
    0
    >>> last_best_win(x, 'AEAAE', 'xynqw', '0000')
    1
    """
    # CASE 0(player 'A' turn):
    # if 1 is inputted and it will
    # make the computation 0 then
    # the result is 1 if inputted 0
    # then do the reverse of it
    if turns[len(values)] == 'A':
        if evaluate(root, variables, values + '1') == 0:
            res = 1
        else:
            res = 0

    # CASE 1(player 'B' turn):
    # if 0 is inputted and it will
    # make the computation 1 then
    # the result is 0 if inputted 1
    # then do the reverse of it
    else:
        if evaluate(root, variables, values + '0') == 1:
            res = 0
        else:
            res = 1

    return res


def partition_negations(root, variables, values):
    """
    (FormulaTree, str, str) -> str
    make a simplified string where
    it signals to current bes move
    for instance if variable x is to
    be assigned the best move then variable
    x will be turned to * and every other
    variable will turn into + and negations
    are also indicated The point of this
    functions is to partition the needed negation
    REQ: len(variables) < len(turns)
    REQ: FormulaTree != None
    REQ: existing variables
    >>> x = build_tree('(((x+y)*(n+q))+(q+w))')
    >>> partition_negations(x, 'xynqw', '1111')
    '+++++*'
    >>> partition_negations(x, 'xynqw', '11')
    '++*+++'
    >>> x = build_tree('--(((--x+y)*(n+q))+--(q+w))')
    >>> partition_negations(x, 'xynqw', '11')
    '--(--++*+--(++'
    """
    # CASE 0('-'):
    # take the children partition
    # the binary operators and the leafs
    # to count the negations correctly
    if root.get_symbol() == '-':
        if root.get_children()[0].get_symbol() == '*' or \
                        root.get_children()[0].get_symbol() == '+':
            v = '-(' + \
                partition_negations(root.get_children()[0], variables, values)
        else:
            v = '-' + \
                partition_negations(root.get_children()[0], variables, values)
    # CASE 1(Binary Operator):
    # take the left and right children
    # add them together if child is the
    # desired then it is a * if common then +
    elif root.get_symbol() == '+' or root.get_symbol() == '*':
        rigth = partition_negations(root.get_children()[0], variables, values)
        left = partition_negations(root.get_children()[1], variables, values)
        v = rigth + left
    # CASE 2(Variable):
    # It is the unique variable
    # we desire meaning this variable
    # decides the best possible move
    # therefore it is represented as '*'
    elif root.get_symbol().islower() \
            and root.get_symbol() in variables \
            and variables[len(values)] == root.get_symbol():
        v = '*'
    # CASE 3(Variable):
    # common variable which
    # is only used for partitioning
    # it is represented as +
    else:
        v = '+'

    return v


def tree2formula(root: 'FormulaTree') -> str:
    """
    Return a string which is the formula represented by the FormulaTree
    rooted at root.
    (Essentially tree2formula is the "inverse" of build_tree.)
    """
    if 'a' <= root.get_symbol() <= 'z':
        result = root.get_symbol()
    elif root.get_symbol() == '-':
        result = '-' + tree2formula(root.get_children()[0])
    else:
        result = '('
        for c in root.get_children():
            result = result + tree2formula(c) + root.get_symbol()
        result = result[:-1] + ')'
    return result


if __name__ == "__main__":
    r = build_tree('(((x+-y)+(x+y))*(x*y))')
    q = build_tree('(--(-a+b)*(-c*d))')
    n = build_tree('(-(h+g)*--(j*k))')
    print(r)
    print(draw_formula_tree(r))
    print(q)
    print(draw_formula_tree(q))
    print(n)
    print(draw_formula_tree(n))
    r = tree2formula(r)
    q = tree2formula(q)
    n = tree2formula(n)
    print(r)
    print(q)
    print(n)
