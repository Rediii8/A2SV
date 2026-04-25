from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):
        n = len(intervals)
        
        starts = sorted((intervals[i][0], i) for i in range(n))
        
        result = [-1] * n
        
        for i, (s, e) in enumerate(intervals):
            
            idx = bisect_left(starts, (e, -1))
            
            if idx < n:
                result[i] = starts[idx][1]
            else:
                result[i] = -1
        
        return result