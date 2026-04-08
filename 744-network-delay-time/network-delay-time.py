import heapq
from collections import defaultdict

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        # строим граф: список смежности
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # приоритетная очередь (мин-куча)
        pq = [(0, k)]
        
        # кратчайшие расстояния
        dist = {}
        
        while pq:
            time, node = heapq.heappop(pq)
            
            # если уже посещали то пропускаем
            if node in dist:
                continue
            
            dist[node] = time
            
            # идем к соседям
            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (time + weight, neighbor))
        
        # если не все вершины достигнуты
        if len(dist) != n:
            return -1
        
        # время равняется максимуму из кратчайших путей
        return max(dist.values())