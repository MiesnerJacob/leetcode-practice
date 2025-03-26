class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head
        prev = None
        while curr:
            if prev == None:
                prev = curr
            elif curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
                
            curr = curr.next
            
        return head
