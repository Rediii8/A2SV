class Solution:
    def maxTurbulenceSize(self, arr):
        n = len(arr)
        if n == 1:
            return 1

        def cmp(a, b):
            if a > b: return 1
            if a < b: return -1
            return 0

        ans = 1
        cur = 1

        for i in range(1, n):
            c = cmp(arr[i-1], arr[i])

            if c == 0:
                cur = 1
            elif i == 1 or c * cmp(arr[i-2], arr[i-1]) != -1:
                
                cur = 2
            else:
               
                cur += 1

            ans = max(ans, cur)

        return ans