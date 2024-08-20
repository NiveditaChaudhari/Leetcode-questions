from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n=len(piles)
        dp=[0]*(n//2+1)
        for i in range(1,n//2+1):
            dp[i]= dp[i-1]+max(piles[i]-piles[n-i], piles[n-i]-piles[i])
        return True

piles=eval(input("Enter the piles list: "))
sol=Solution()
print("Ans: ",sol.stoneGame(piles))

