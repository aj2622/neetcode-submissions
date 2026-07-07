# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        head = temp = ListNode(-float('inf'), None)
        
        while list1 and list2:

            if list1.val <= list2.val:
                # cut list1 
                nxt = list1
                # advance list1 
                list1 = list1.next
            else:
                # cut list2
                nxt = list2
                # advance list2
                list2 = list2.next
            # point temp.next to nxt
            temp.next = nxt
            # update temp
            temp = temp.next

        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        

        return head.next