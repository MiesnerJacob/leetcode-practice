class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = []
        for i in range(len(intervals)):
            if not result or intervals[i][0] > result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1]=max(result[-1][1],intervals[i][1])
        return result 