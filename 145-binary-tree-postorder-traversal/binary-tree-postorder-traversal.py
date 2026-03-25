# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        result = []  # список для результата
        
        def dfs(node):
            # если узел пустой
            if not node:
                return
            
            dfs(node.left)           # левое поддерево
            dfs(node.right)          # правое поддерево
            result.append(node.val)  # сначала корень
        
        dfs(root)
        return result