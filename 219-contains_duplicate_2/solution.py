class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}

        for index, value in enumerate(nums):
          if value in d and abs(index - d[value]) <= k:
            return True
          else:
            d[value] = index
        
        return False