from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        new_arr=[]
        length=len(nums)
        for i in range(length):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j,k=i+1,length-1
            while j<k:
                total = nums[i]+nums[j]+nums[k]
                if total==0:
                    new_arr.append([nums[i],nums[j],nums[k]])

                    while j<k and nums[j] == nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    
                    j+=1
                    k-=1
                elif total<0:
                    j+=1
                else:
                    k-=1

        return new_arr
    

nums=eval(input("Enter numbers separated by spaces: ")) #[-1,0,1,2,-1,-4]
sol = Solution()
print("Index are: ",sol.threeSum(nums))

# Complexity: O(N^2)