# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        fast and slow pointers to find middle of the list, 
        when fast at end, slow at middle

        then reverse second half of list

        then weave together values
        """

        # base case of linked list with one or two nodes
        if not head or not head.next:
            return 

        # find middle of list
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # slow points at halfway, fast points at end

        # reverse list helper function
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        # reverse second half of list
        reversed = reverseList(slow.next)
        slow.next = None

        og = head

        while reversed:
            temp1 = og.next
            temp2 = reversed.next
            
            og.next = reversed
            reversed.next = temp1

            og = temp1
            reversed = temp2


