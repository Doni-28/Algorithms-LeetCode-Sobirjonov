class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        total = sum(nums)
        
        # Если сумма нечётная нельзя разделить
        if total % 2 != 0:
            return False
        
        target = total // 2
        
        # dp[i] можно ли получить сумму i
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            # идём с конца, чтобы не использовать число повторно
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]