class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        
        
        self.prefix = [0] * (n + 1)

        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]