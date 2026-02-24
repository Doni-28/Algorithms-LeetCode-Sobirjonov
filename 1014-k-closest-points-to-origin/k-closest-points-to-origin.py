import heapq

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # max heap, хранит отрицательные квадраты дистанций
        heap = []
        
        for x, y in points:
            dist = -(x*x + y*y)  # квадрат расстояния
            if len(heap) < k:
                heapq.heappush(heap, (dist, [x, y]))
            else:
                # если новая точка ближе, чем самая дальняя в куче
                if dist > heap[0][0]:  # dist меньше по модулю
                    heapq.heappushpop(heap, (dist, [x, y]))
        
        # остаются k ближайших точек
        return [point for (_, point) in heap]