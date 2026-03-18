class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window_size = 2 * k + 1
        
        
        avgs = [-1] * n
        
        
        if window_size > n:
            return avgs
        
      
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
       
        for i in range(k, n - k):
            total = prefix[i + k + 1] - prefix[i - k]
            avgs[i] = total // window_size
        
        return avgs       