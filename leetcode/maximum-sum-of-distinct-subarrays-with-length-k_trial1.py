class Solution:
    def maximumSubarraySum(self, nums, k):
        left = 0
        freq = {}
        current_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            # add right element
            current_sum += nums[right]
            freq[nums[right]] = freq.get(nums[right], 0) + 1

            # shrink if window > k
            if right - left + 1 > k:
                freq[nums[left]] -= 1
                current_sum -= nums[left]
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # check valid window
            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum     