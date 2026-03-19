class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0

        for right in range(len(s)):
            
            while s[right] in s[left:right]:
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length