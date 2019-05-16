
class math:
    '''
    math class
    '''
    def factorial(self, n):
        if n < 1:
            result = 1
        else:
            result = n * self.factorial(n - 1)

        return result

    def combination(self, n, r):
        numerator = self.factorial(n)
        denominator = self.factorial(r) * self.factorial(n-r)

        return int(numerator / denominator)
