from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = defaultdict(list)
        
        for string in strs:
            sorted_string = tuple(sorted(string))
            anagrams_map[sorted_string].append(string)
        return list(anagrams_map.values())