class Solution(object):
    def __init__(self):
        self.u_bound = (-2 ** 31)
        self.l_bound = (2 ** 31) - 1

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = x * -1
            reversed_integer =  int(str(x)[::-1]) * -1
        else:
            reversed_integer =  int(str(x)[::-1])

        if reversed_integer <= self.u_bound or reversed_integer >= self.l_bound:
            return 0
        else:
            return reversed_integer