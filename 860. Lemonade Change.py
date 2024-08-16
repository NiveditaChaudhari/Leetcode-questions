from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change={5:0,10:0}
        val=0
        for i in bills:
            if i==5:
                change[5]+=1
            elif i==10:
                if change[5]>0:
                    change[10]+=1
                    change[5]-=1    
                else:
                    return False
            elif i==20:
                if change[10]>0 and change[5]>0:
                    change[10]-=1
                    change[5]-=1
                elif change[5]>=3:
                    change[5]-=3   
                else:
                    return False
        return True

sol=Solution()
bill=eval(input("Enter the array: "))
print(sol.lemonadeChange(bill))