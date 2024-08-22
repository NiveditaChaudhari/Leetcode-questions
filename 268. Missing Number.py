from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # length=len(nums)
        # for i in range(0,length+1):
        #     if i not in nums:
        #         mis_no=i

        n=set(range(len(nums)+1))
        nums_set=set(nums)
        mis_no=n-nums_set
        return mis_no.pop()

nums=eval(input("Enter the number: "))
sol=Solution()
print("Ans: ", sol.missingNumber(nums))