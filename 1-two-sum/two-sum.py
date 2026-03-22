class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}  # словарь
        
        for i in range(len(nums)):
            complement = target - nums[i]  # число, которое нужно найти
            
            # увидели нужное число — возвращаем ответ
            if complement in hashmap:
                return [hashmap[complement], i]
            
            # сохраняем текущее число в словарь
            hashmap[nums[i]] = i