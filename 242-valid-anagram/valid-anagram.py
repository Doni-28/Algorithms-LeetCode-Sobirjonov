class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # если длины разные —  false
        if len(s) != len(t):
            return False
        
        count = {}  # словарь для подсчёта символов
        
        # считаем символы в строке s
        for char in s:
            count[char] = count.get(char, 0) + 1
        
        # уменьшаем счётчики по строке t
        for char in t:
            if char not in count:
                return False
            count[char] -= 1
            if count[char] < 0:
                return False
        
        return True
    