# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head.next, head

        # Find the end of the first half
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second = slow.next
        slow.next = None

        # Reverse second list
        prev = None
        while second:
            # Save where second will move next
            temp = second.next
            # Reverse the arrow
            second.next = prev
            # Move the prev pointer to the next node (current node)
            prev = second
            # Move the second pointer to the next node (temp)
            second = temp

        first = head
        second = prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        return second
        