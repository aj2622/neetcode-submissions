# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        arr = deque([])
        nxt = head.next
        while nxt:
            arr.append(nxt)
            nxt = nxt.next
        
        nxt = head
        while arr:
            nxt.next = arr.pop()
            nxt = nxt.next
            if arr:
                nxt.next = arr.popleft()
                nxt = nxt.next
        nxt.next = None 