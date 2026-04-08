class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        
        # исходный цвет пикселя
        original = image[sr][sc]
        
        # если цвет такой же ничего не делаем
        if original == color:
            return image
        
        def dfs(r, c):
            # проверка выхода за границы
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            
            # если цвет не совпадает не трогаем
            if image[r][c] != original:
                return
            
            # перекрашиваем пиксель
            image[r][c] = color
            
            # идём в 4 направления (вверх, вниз, вправо, влево)
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # запускаем DFS от стартовой точки
        dfs(sr, sc)
        
        return image