class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        list1 = list(word1)
        list2 = list(word2)

        output = []
        for val1, val2 in zip(list1, list2):
            output.append(val1)
            output.append(val2)

        if len(list1) == len(list2):
            return "".join(output)
        elif len(list1) < len(list2):
            return "".join(output + list2[len(list1):])
        else:
            return "".join(output + list1[len(list2):])
        