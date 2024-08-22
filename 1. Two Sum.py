from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        while i<len(nums):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
            else:
                i+=1
        else:
            return "Not present"

nums=eval(input("Enter numbers separated by spaces: "))
target=int(input("Target Sum: "))
sol = Solution()
print("Index are: ",sol.twoSum(nums,target))