from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        curr=float('inf')
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,len(nums)-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==target:
                    return total
                
                if abs(total-target) < abs(curr-target):
                    curr=total
                    
                elif total < target:
                    j+=1
                else:
                    k-=1
        return curr

nums=eval(input("Enter numbers separated by spaces: ")) 
target = int(input("Target value: "))
sol = Solution()
print("Closest sum is: ",sol.threeSumClosest(nums,target))

                