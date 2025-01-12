class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort(key=len)

        longest_common_prefix = ""
        for i in range(len(strs[0])):
            if len(set([j[i] for j in strs])) == 1:
                longest_common_prefix = strs[0][:i + 1]
            else:
                return longest_common_prefix
        
        return longest_common_prefix