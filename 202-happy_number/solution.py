class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        already_seen = set()
        while n != 1:
            if n in already_seen: 
                return False
            
            already_seen.add(n)
            n = sum([int(i) ** 2 for i in str(n)])
        else:
            return True