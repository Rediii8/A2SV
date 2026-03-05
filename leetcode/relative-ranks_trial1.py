class Solution:
    def findRelativeRanks(self, score):
        n = len(score)
        
       
        athletes = [(s, i) for i, s in enumerate(score)]
        
        
        athletes.sort(reverse=True)
        
        answer = [""] * n
        
        for rank, (_, index) in enumerate(athletes):
            if rank == 0:
                answer[index] = "Gold Medal"
            elif rank == 1:
                answer[index] = "Silver Medal"
            elif rank == 2:
                answer[index] = "Bronze Medal"
            else:
                answer[index] = str(rank + 1)
        
        return answer