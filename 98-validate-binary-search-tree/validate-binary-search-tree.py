# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def dfs(node, left, right):
            # если узел пустой — это корректно
            if not node:
                return True
            
            # проверяем, входит ли значение в допустимый диапазон
            if not (left < node.val < right):
                return False
            
            # проверяем левое и правое поддерево
            return (dfs(node.left, left, node.val) and
                    dfs(node.right, node.val, right))
        
        return dfs(root, float('-inf'), float('inf'))