class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        indices = []
        for index, value in enumerate(nums):
            if value == val:
                indices.append(index)

        indices.sort(reverse=True)

        for index in indices:
            nums.pop(index)
