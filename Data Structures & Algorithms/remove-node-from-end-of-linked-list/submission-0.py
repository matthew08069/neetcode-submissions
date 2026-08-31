# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find the nth node
        dummy = ListNode(0, head)
        left, right = dummy, dummy
        for _ in range(n+1):
            right = right.next
        
        while right:
            left = left.next
            right = right.next

        # Find the n-1th node and link it to the n+1th node
        left.next = left.next.next
        return dummy.next