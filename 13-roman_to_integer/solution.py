class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        last_value = None

        for char in list(s):
            current_value = mapping[char]
            total += current_value
            if last_value and last_value < current_value:
                total -= last_value * 2
            print(total)
            last_value = current_value

        return total
