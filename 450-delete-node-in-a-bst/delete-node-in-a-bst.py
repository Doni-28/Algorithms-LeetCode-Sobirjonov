# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        
        # если дерево пустое
        if not root:
            return None
        
        # ищем узел
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            # узел найден
            
            # нет левого ребёнка
            if not root.left:
                return root.right
            
            # нет правого ребёнка
            if not root.right:
                return root.left
            
            # два ребёнка
            # находим минимальный в правом поддереве
            temp = root.right
            while temp.left:
                temp = temp.left
            
            # заменяем значение
            root.val = temp.val
            
            # удаляем дубликат
            root.right = self.deleteNode(root.right, temp.val)
        
        return root