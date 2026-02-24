import heapq
from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #  частота чисел
        count = Counter(nums)  # {число: частота}
        
        # min heap размера k
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            
            # Если размер > k, удаляем минимальный
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for freq, num in heap]