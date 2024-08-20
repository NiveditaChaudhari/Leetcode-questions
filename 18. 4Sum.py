from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        new_arr=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                k,l=j+1, len(nums)-1
                while k<l:
                    total = nums[i]+nums[j]+nums[k]+nums[l]
                    if total == target:
                        new_arr.append([nums[i],nums[j],nums[k],nums[l]])

                        while k<l and nums[k] == nums[k+1]:
                            k+=1
                        while k<l and nums[l] == nums[l-1]:
                            l-=1
                        k+=1
                        l-=1

                    elif total<target:
                        k+=1
                    else:
                        l-=1
        return new_arr




nums=eval(input("Enter numbers separated by spaces: ")) #[1,0,-1,0,-2,2]
target = int(input("Target value: "))
sol = Solution()
print("Four sum is: ",sol.fourSum(nums,target))