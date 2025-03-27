class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for index, value in enumerate(numbers):
            remainder = target - value
            if remainder in d:
                return [d[remainder] + 1, index + 1]
            d[value] = index