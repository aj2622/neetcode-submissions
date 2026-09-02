# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        zeroNode = ListNode(0, head)

        # count len of list
        start = head
        l = 0
        while start:
            l += 1
            start = start.next
        
        # go to the right node and remove the next element
        start = zeroNode
        index = l - n
        i = 0
        while i != index:
            i += 1
            start = start.next
        print(start.val)
        start.next = start.next.next

        return zeroNode.next