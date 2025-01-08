class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = sorted(nums1 + nums2)
        nums3_len = len(nums3)
        if nums3_len % 2 == 0:
            return (nums3[nums3_len // 2] + nums3[nums3_len // 2 - 1]) / 2.0
        else:
            return nums3[nums3_len // 2]