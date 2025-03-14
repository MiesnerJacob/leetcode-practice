class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        h_index = 0
        c = sorted(citations, reverse=True)
        for index, value in enumerate(c):
            if index < value:
                h_index +=1
            else:
                return h_index
        return h_index
