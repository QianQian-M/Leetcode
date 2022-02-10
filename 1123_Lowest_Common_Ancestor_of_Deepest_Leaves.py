# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        # def helper(root):
        #     if not root: return 0, None
        #     h1, lca1 = helper(root.left)
        #     h2, lca2 = helper(root.right)
        #     if h1 > h2: return h1 + 1, lca1
        #     if h1 < h2: return h2 + 1, lca2
        #     return h1 + 1, root
        # return helper(root)[1]
  
        def dfs(node):
            
            if not node:
                return None,0
            
            LCA_l, l=dfs(node.left) 
            
            LCA_r, r=dfs(node.right)
            
            # if l = r, it means in the same level, just keep searching
            
            if l > r: return LCA_l,l+1
            if l < r: return LCA_r,r+1
            
            return node,l+1
            