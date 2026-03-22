class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        seen = set()  # множество для хранения уже встреченных элементов
        
        for num in nums:
            # если элемент уже есть — найден дубликат
            if num in seen:
                return True
            
            # добавляем элемент в множество
            seen.add(num)
        
        return False