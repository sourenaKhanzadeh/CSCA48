'''
Abstract data types
-------------------
An abstract data type, or ADT,
specifies a set of operations (or methods) and the semantics of the
operations (what they do), but it does not not specify the
implementation of the operations. That’s what makes it abstract.

Why is that useful?
------------------
1.It simplifies the task of specifying an algorithm if
you can denote the operations you need without having to think at
the same time about how the operations are performed.

2. Since there are usually many ways to implement an ADT,
it might be useful to write an algorithm
that can be used with any of the possible implementations.

3. Well-known ADTs, such as the Stack ADT in this
chapter, are often implemented in standard
libraries so they can be written once and used by many programmers.

4. The operations on ADTs provide a common high-level
language for specifying and talking about algorithms.

When we talk about ADTs, we often distinguish between the code
that uses the ADT, called the client code, from the code that
implements the ADT, called the provider/implementor code

The operation that can be performed on the ADT is called the interface

A stack is sometimes called a “Last in, First out” or
LIFO data structure, because the last item added is the first to be removed.

This code is called an implementation of the Stack ADT. In general, an implementation is a
set of methods that satisfy the syntactic and semantic requirements of an interface.
Here is an implementation of the Stack ADT that uses a Python list:

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return (self.items == [])

A stack is a generic data structure, which means that we can add
any type of item to it. The following example pushes two integers and a string onto the stack:

    # >>> s = Stack()
    # >>> s.push(54)
    # >>> s.push(45)
    # >>> s.push("+")

In most programming languages, mathematical expressions are
written with the operator between the two operands, as in 1 + 2. This format is called infix.
An alternative used by some calculators is called postfix. In postfix, the operator follows the operands, as in 1 2 +.

The reason postfix is sometimes useful is that there is a natural way to evaluate a postfix expression using a stack:

Starting at the beginning of the expression, get one term (operator or operand) at a time.

1.If the term is an operand, push it on the stack.
If the term is an operator, pop two operands off the stack,
 perform the operation on them, and push the result back on the stack.

2.When you get to the end of the expression,
 there should be exactly one operand left on the stack. That operand is the result.

Parsing
To implement the previous algorithm, we need to be able to
traverse a string and break it into operands and operators.
This process is an example of parsing, and the results — the individual chunks of the string
— are called tokens. You might remember these words from Chapter 1.

Python provides a split method in both string objects and the
 re (regular expression) module. A string’s split method splits
  it into a list using a single character as a delimiter. For example:

# >>> "Now is the time".split(" ")
['Now', 'is', 'the', 'time']

Glossary
---------
abstract data type (ADT)
A data type (usually a collection of objects) that is defined
by a set of operations but that can be implemented in a variety of ways.

client
A program (or the person who wrote it) that uses an ADT.

delimiter
A character that is used to separate tokens, such as punctuation in a natural language.

generic data structure
A kind of data structure that can contain data of any type.

implementation
Code that satisfies the syntactic and semantic requirements of an interface.

interface
The set of operations that define an ADT.

infix
A way of writing mathematical expressions with the operators between the operands.

parse
To read a string of characters or tokens and analyze its grammatical structure.

postfix
A way of writing mathematical expressions with the operators after the operands.

provider
The code (or the person who wrote it) that implements an ADT.
token
A set of characters that are treated as a unit for purposes of parsing, such as the words in a natural language.

veneer
A class definition that implements an ADT with method definitions that are
invocations of other methods, sometimes with simple transformations.
The veneer does no significant work, but it improves or standardizes the interface seen by the client.

• Data:
    • Any arbitrary objects/elements
    • Operations:
    • Main:
        • push(e): add element e to the front/head of the stack
        • pop(): remove and return the element from the front/head of the queue
    • Auxiliary:
        • top(): returns the element at the front without removing it
        • size(): returns the number of elements in the queue
        • is_empty(): indicates whether or not the queue is empty
• Exception:
    • Raise EmptyStackException if the stack is empty and pop() or top() is requested
'''


class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return "{}".format(stack.get_stack())

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items

    def eval_postfix(expr):
        # to evaluate postfix expression
        import re
        # split the operators
        token_list = re.split("([^0-9])", expr)
        stack = Stack()
        for token in token_list:
            if token == "" or token == " ":
                continue
            if token == "+":
                sum = stack.pop() + stack.pop()
                stack.push(sum)
            elif token == "*":
                product = stack.pop() * stack.pop()
                stack.push(product)
            else:
                stack.push(int(token))
        return stack.pop()

if __name__ == "__main__":
    stack = Stack()
    print(stack)
