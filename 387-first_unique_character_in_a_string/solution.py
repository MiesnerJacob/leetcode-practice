class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts = {}

        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

        for index, value in enumerate(list(s)):
            if char_counts[value] > 1:
                continue
            else:
                return index
        return -1