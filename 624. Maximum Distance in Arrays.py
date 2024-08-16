from typing import List

class Solution:
    def maxDistance(self, arr: List[List[int]]) -> int:
        max_val,min_val=max(arr[0]),min(arr[0])
        max_dis=0
        for i in range(1,len(arr)):
            curr_min = min(arr[i])
            curr_max = max(arr[i])
            max_dis = max(max_dis,abs(max_val-curr_min), abs(min_val-curr_max))
            min_val = min(min_val, curr_min)  
            max_val = max(max_val, curr_max)
        return max_dis

arr=eval(input("Enter the list: "))
sol=Solution()
print("Maximum value is: ",sol.maxDistance(arr))