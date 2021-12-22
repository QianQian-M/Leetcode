# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
  
        
        node_val =[]
        
        for i in lists:
            while i:
                node_val.append(i.val)
                i = i.next
        
        res = sorted(node_val)
        head = res_node = ListNode(0)
        for v in res:
            
            res_node.next = ListNode(v)
            res_node = res_node.next
        
        return head.next
           