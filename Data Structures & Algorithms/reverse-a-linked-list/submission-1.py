# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next is None: 
            return head

        curr = head
        while curr.next.next: # get to second to last element of list
            curr = curr.next

        new_head = curr.next # set last obj to new head
        curr.next = curr.next.next # last object null
        
        new_head.next = self.reverseList(head)

        return new_head