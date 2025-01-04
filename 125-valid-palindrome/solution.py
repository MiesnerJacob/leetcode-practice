import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_mod = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        steps = len(s_mod) // 2
        for i in range(steps):
            valid = s_mod[i] == s_mod[~i]
            if not valid:
                return False
        return True