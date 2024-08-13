from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        med=0
        num=sorted(nums1+nums2)
        n=len(num)
        if len(num)%2==0:
            mid_index1 = n // 2
            mid_index2 = mid_index1 - 1 
            med=(num[mid_index1]+num[mid_index2])/2
        elif len(num)%2!=0:
            mid_index1 = n // 2
            med=num[mid_index1]
        return float(med)
    

nums1=eval(input("Enter numbers separated by spaces: "))
nums2=eval(input("Enter numbers separated by spaces: "))
sol = Solution()
print("Index are: ",f"{sol.findMedianSortedArrays(nums1,nums2):.4f}")