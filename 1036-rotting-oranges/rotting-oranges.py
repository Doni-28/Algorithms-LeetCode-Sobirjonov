from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        fresh = 0
        
        # собираем все гнилые апельсины и считаем свежие
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (строка, столбец, время)
                elif grid[r][c] == 1:
                    fresh += 1
        
        time = 0
        
        # BFS
        while queue:
            r, c, t = queue.popleft()
            time = max(time, t)
            
            # 4 направления
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr = r + dr
                nc = c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, t + 1))
        
        # если остались свежие то невозможно
        return time if fresh == 0 else -1