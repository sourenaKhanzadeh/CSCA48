'''
5th pos
-------
1
11
121
1331
14641
'''
from Compsci_II.Practices.my_math import *

mt = math()


class PascalsTriangle:
    '''
    A class that creates pascals
    triangle
    '''

    def make_rows(self, n, r=0):
        '''
        1 index = 0
        11 index = 1
        121 index = 2
        1331 index = 3
        '''
        if n < r:
            pass
        else:
            res = mt.combination(n, r)
            print(str(res), end=' ')
            # if r != n:
            self.make_rows(n, r + 1)
        return ''

    def make_triangle(self, n, r=0):
        if r == n:
            pass
        else:
            res = self.make_rows(r)
            print(res, end='\n')
            self.make_triangle(n, r + 1)


class Fibonacci:

    def make_fib(self):
        a, b = 0, 1
        while True:
            yield b
            a, b = b, a + b

    def fib(self, n):
        f = self.make_fib()
        return [next(f) for i in range(n)]

if __name__ == '__main__':
    p = PascalsTriangle()
    f = Fibonacci()
    f.fib(100)
