# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lst1 = []
        lst2 = []

        current_l1 = l1
        while current_l1:
            lst1.append(current_l1.val)
            current_l1 = current_l1.next

        current_l2 = l2
        while current_l2:
            lst2.append(current_l2.val)
            current_l2 = current_l2.next

        lst1_reverse = lst1[::-1]
        lst2_reverse = lst2[::-1]

        num1 = "".join([str(i) for i in lst1_reverse])
        num2 = "".join([str(i) for i in lst2_reverse])

        new_num = int(num1) + int(num2)

        new_num_lst = list(str(new_num))
        new_num_list_reverse = new_num_lst[::-1]
        
        dummy = ListNode()
        current = dummy
        for digit in new_num_list_reverse:
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next