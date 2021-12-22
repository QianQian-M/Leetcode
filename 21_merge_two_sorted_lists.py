# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1 and not list2: 
            return list1
        elif not list1: 
            return list2
        elif not list2:
            return list1
        
        head = ListNode()
        res = head
        while list2 and list1:
            
            if list2.val >= list1.val:
                l1_next = list1.next
                list1.next =None
                head.next = list1
                head = list1
                list1=l1_next
            else:
                l2_next = list2.next
                list2.next = None
                head.next = list2
                head = list2
                list2=l2_next
        
          
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        return res.next   
                
          
# Solution: Concise

class Solution:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next