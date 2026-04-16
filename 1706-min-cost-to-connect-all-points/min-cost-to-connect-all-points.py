class Solution(object):
    def minCostConnectPoints(self, points):
        import heapq
        
        n = len(points)
        visited = [False] * n
        min_heap = [(0, 0)]  # стоимость и индекс точки
        
        result = 0
        edges_used = 0
        
        while edges_used < n:
            cost, i = heapq.heappop(min_heap)
            
            # если уже посещали то пропускаем
            if visited[i]:
                continue
            
            visited[i] = True
            result += cost
            edges_used += 1
            
            # добавляем все возможные рёбра
            for j in range(n):
                if not visited[j]:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(min_heap, (dist, j))
        
        return result