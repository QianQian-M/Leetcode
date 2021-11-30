# need to walk trees, preorder, inorder, postorder
# need to store unique subtrees somewhere Map/Set
# need unique key for subtree hash(key left + key right + val)
# handle hash conflicts?
# use hashmap to store monotonic id for (key left + key right + val)
# parent uses left child's mono id + right child's mono id + val

# First Solution, much faster, using id
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        subtrees = {}
        mono_id = 1
        visited = set()
        res = []
        def helper(node: TreeNode) -> int:
            nonlocal mono_id
            if not node:
                return 0
            left_id = helper(node.left)
            right_id = helper(node.right)
            key = (node.val, left_id, right_id)
            if key in subtrees:
                # already seen this unique subtree
                if key not in visited:
                    # first time re-visiting this unique subtree
                    visited.add(key)
                    res.append(node)
            else:
                # first time seeing this unique subtree
                subtrees[key] = mono_id
                mono_id += 1
            return subtrees[key]
        helper(root)
        return res


# Second Solution: Serilization
# two coding styles

#<1>
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        res = []
        
        hmap = {}
        
        def recurse(node, path):
            if node is None:
                return '#'
            
            path += ','.join([str(node.val), recurse(node.left, path), recurse(node.right, path)])
            
            if path in hmap:
                hmap[path] += 1
                if hmap[path] == 2:
                    res.append(node)
            else:
                hmap[path] = 1
                
            
            return path
        
        recurse(root, '')
        #print(hmap) I SUGGEST YOU PRINT THIS - TO UNDERSTAND WHAT IS HAPPENING.
        return res

#<2>
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        data = defaultdict(int)
        ans = []
        def traverse(node):
            if not node:
                return "."
            subtree = traverse(node.left) + "*" + traverse(node.right) + "*" + str(node.val)
            if data[subtree] == 1:
                ans.append(node)
            data[subtree] += 1
            return subtree
        traverse(root)
        return ans