class Solution:
    def smallestDivisor(self, nums, threshold):
        left, right = 1, max(nums)
        
        def compute_sum(d):
            return sum((num + d - 1) // d for num in nums)
        
        while left < right:
            mid = (left + right) // 2
            
            if compute_sum(mid) <= threshold:
                right = mid
            else:
                left = mid + 1
        
        return left