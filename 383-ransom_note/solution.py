from collections import defaultdict

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for i in ransomNote:
            d1[i] += 1
        for i in magazine:
            d2[i] += 1

        for key, value in d1.items():
            if value > d2[key]:
                return False
        return True



