from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # Create a suffix sum array for quick calculation of the remaining stones
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]

        @lru_cache(None)
        def solveforAlice(i: int, M: int) -> int:
            if i == n:
                return 0
            if 2 * M >= n - i:
                return suffix_sum[i]
            
            max_stone = float('-inf')
            for x in range(1, 2 * M + 1):
                max_stone = max(max_stone, suffix_sum[i] - solveforAlice(i + x, max(M, x)))
            return max_stone

        return solveforAlice(0, 1)

# Example usage:
piles = [2, 7, 9, 4, 4]
sol = Solution()
print("Ans: ", sol.stoneGameII(piles))  # Expected output: 10
