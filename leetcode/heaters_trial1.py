import bisect

class Solution:
    def findRadius(self, houses, heaters):
        houses.sort()
        heaters.sort()
        
        res = 0
        
        for house in houses:
            
            idx = bisect.bisect_left(heaters, house)
            
            
            left_dist = float('inf')
            if idx > 0:
                left_dist = house - heaters[idx - 1]
            
            
            right_dist = float('inf')
            if idx < len(heaters):
                right_dist = heaters[idx] - house
            
           
            closest = min(left_dist, right_dist)
            
           
            res = max(res, closest)
        
        return res