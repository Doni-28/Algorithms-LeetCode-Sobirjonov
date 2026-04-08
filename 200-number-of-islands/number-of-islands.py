class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        
        def dfs(r, c):
            # проверка границ
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            
            # если это вода, выходим
            if grid[r][c] == '0':
                return
            
            # затапливаем землю, чтобы не считать повторно
            grid[r][c] = '0'
            
            # идем в 4 направления
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1
        
        return islands