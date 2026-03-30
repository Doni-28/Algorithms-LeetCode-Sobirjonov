# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        
        # если дерево пустое, создаём новый узел
        if not root:
            return TreeNode(val)
        
        # если значение меньше, идём влево
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        
        # если больше, идём вправо
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        # возвращаем корень дерева
        return root