class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        number_str = ""
        is_neg = 1

        for index, value in enumerate(list(s.lstrip())):
            if index == 0 and value == "-":
                is_neg = -1 
                continue
            if index == 0 and value == "+":
                continue
            if value in ["0","1","2","3","4","5","6","7","8","9"]:
                number_str += value
            else:
                break
        
        if number_str == "":
            return 0

        final_number = int(number_str) * is_neg

        if final_number < (-2 ** 31):
            return (-2 ** 31)
        elif final_number > (2 ** 31 -1):
            return (2 ** 31 -1)
        else:
            return final_number
