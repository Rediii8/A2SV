class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        whites = blocks[:k].count('W')
        ans = whites

        
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                whites += 1
            if blocks[i - k] == 'W':
                whites -= 1

            ans = min(ans, whites)

        return ans