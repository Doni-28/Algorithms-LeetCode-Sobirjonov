class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        hashmap = {}  # ключ: отсортированная строка, значение: список анаграмм
        
        for word in strs:
            # создаём ключ — сортируем буквы в слове
            key = ''.join(sorted(word))
            
            # если ключа ещё нет — создаём новый список
            if key not in hashmap:
                hashmap[key] = []
            
            # добавляем слово в соответствующую группу
            hashmap[key].append(word)
        
        # возвращаем все группы анаграмм
        return list(hashmap.values())