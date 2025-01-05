class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for index, value in enumerate(nums):
            d.setdefault(value, index)

        for index, value in enumerate(nums):
            remainder = target - value
            if remainder in d and d[remainder] != index:
                return [index, d[remainder]]
            