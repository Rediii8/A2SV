class Solution:
    def relativeSortArray(self, arr1, arr2):
        from collections import Counter
        
        count = Counter(arr1)
        result = []
        
        for num in arr2:
            result.extend([num] * count[num])
            count.pop(num)
        
        remaining = []
        for num in sorted(count.keys()):
            remaining.extend([num] * count[num])
        
        return result + remaining