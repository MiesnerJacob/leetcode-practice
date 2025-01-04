from collections import defaultdict

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map = defaultdict(list)
        t_map = defaultdict(list)

        if len(s) != len(t):
            return False

        for c1, c2 in zip(s,t):
            if c2 not in s_map[c1]:
                s_map[c1].append(c2)
            if c1 not in t_map[c2]:
                t_map[c2].append(c1)
        
        for value in s_map.values():
            if len(value) > 1:
                return False

        for value in t_map.values():
            if len(value) > 1:
                return False
            
        return True