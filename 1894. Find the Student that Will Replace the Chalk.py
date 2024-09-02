from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total_chalk=sum(chalk)
        k%=total_chalk
        for i in range(len(chalk)):
            if k<chalk[i]:
                return i
            k-=chalk[i]
        return -1
        
chalk = eval(input(("List input: ")))
k = int(input("K value: "))
sol=Solution()
print("Ans: ",sol.chalkReplacer(chalk,k))