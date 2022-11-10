# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
        
        
        
        
        
        
        
#         prev = None
#         while head and head.next:
#             cur = head.next
#             head.next = prev
#             prev = head
#             head = cur
#         if head:
#             head.next = prev
            
#         return head