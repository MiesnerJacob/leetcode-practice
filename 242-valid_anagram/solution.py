class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_freq = {}
        t_freq = {}

        if len(s) != len(t):
            return False

        for i in s:
            s_freq[i] = s_freq.get(i, 0) + 1

        for i in t:
            t_freq[i] = t_freq.get(i, 0) + 1

        for key, value in s_freq.items():
            if key not in t_freq:
                return False
            elif value != t_freq[key]:
                return False
        return True