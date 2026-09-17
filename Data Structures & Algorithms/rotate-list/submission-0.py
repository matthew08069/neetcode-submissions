# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head

        n = 0
        cur = head

        while cur:
            n += 1
            cur = cur.next
       
        cur = head
        k =  k % n
        if k == 0:
            return head
        cut = n - k

        for _ in range(cut - 1):
            cur = cur.next

        new_tail = cur
        new_head = cur.next
        new_tail.next = None
        cur = new_head

        while cur is not None:
            if cur.next == None:
                cur.next = head
                break
            cur = cur.next

        return new_head 