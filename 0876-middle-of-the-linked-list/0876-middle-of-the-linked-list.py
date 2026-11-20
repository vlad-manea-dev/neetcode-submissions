# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1


        length = length // 2
        cur = head
        while length:
            cur = cur.next
            length -= 1
        return cur