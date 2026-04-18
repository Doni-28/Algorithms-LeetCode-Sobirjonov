class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # prev максимум до позапрошлого дома
        # curr максимум до предыдущего дома
        prev, curr = 0, 0
        
        for num in nums:
            # временно сохраняем текущее значение
            temp = curr
            
            # выбираем: грабить или пропустить
            curr = max(curr, prev + num)
            
            # сдвигаем prev
            prev = temp
        
        return curr