# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        result = []  # список для хранения результата
        
        def dfs(node):
            # если узел пустой — ничего не делаем
            if not node:
                return
            
            dfs(node.left)          # идём в левое поддерево
            result.append(node.val) # добавляем значение узла
            dfs(node.right)         # идём в правое поддерево
        
        dfs(root)
        return result