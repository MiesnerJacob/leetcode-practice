class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        str_list = [str(i) for i in digits]
        joined_str = "".join(str_list)
        num = int(joined_str)
        num += 1
        num_str = str(num)
        num_str_list = list(num_str)
        return [int(i) for i in num_str_list]