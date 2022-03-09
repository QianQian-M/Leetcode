# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
            1. sorting for final res
            2. without sorting for final res
        '''
        if not root:return []
        d ={}
        
        q = deque([(root,0)],)
        
        while q:
            current, idx = q.popleft()
            
            if idx not in d:
                d[idx]=[]
            d[idx].append(current.val)
            
            if current.left:
                q.append([(current.left),idx-1])
            if current.right:
                q.append([(current.right),idx+1])
        
        #         return [columnTable[x] for x in sorted(columnTable.keys())] from solution
        # print(sorted(d.keys()))
        res=[]
        for x in sorted(d.items(), key= lambda x:x[0]):
            res.append(x[1])
            
        return res
                
                