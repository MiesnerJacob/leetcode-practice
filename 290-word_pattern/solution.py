from collections import defaultdict

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_dict = defaultdict(list)
        s_dict = defaultdict(list)

        s_words = s.split(" ")
        
        if len(pattern) != len(s_words):
            return False

        for c1, c2 in zip(pattern, s_words):
            if c2 not in pattern_dict[c1]:
                pattern_dict[c1].append(c2)
            if c1 not in s_dict[c2]:
                s_dict[c2].append(c1)

        for value in pattern_dict.values():
            if len(value) > 1:
                return False

        for value in s_dict.values():
            if len(value) > 1:
                return False

        return True