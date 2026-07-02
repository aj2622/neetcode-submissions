# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        arr = []
        nxt = head
        while nxt:
            arr.append(nxt)
            nxt = nxt.next
        
        n = len(arr)
        ans_idx = [0]
        dq = deque([i for i in range(1,n)])
        while dq:
            ans_idx.append(dq.pop())
            if dq:
                ans_idx.append(dq.popleft())
        print(ans_idx)
         
        temp = head
        for nxt in ans_idx[1:]:
            temp.next = arr[nxt]
            temp = arr[nxt]

        temp.next = None