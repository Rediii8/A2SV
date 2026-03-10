class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        winsum = sum(nums[:k])
        maxsum = winsum
        for i in range(k, len(nums)):
            winsum += nums[i] - nums[i-k]
            maxsum = max(maxsum, winsum)
        return maxsum/k
    

        