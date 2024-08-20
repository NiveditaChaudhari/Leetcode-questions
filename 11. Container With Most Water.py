from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        max_area=0
        while start<end:
            max_area = max(max_area,(end-start)*min(height[start],height[end]))
            if height[start]<height[end]:
               start+=1
            else:
                end-=1
        return max_area

height=eval(input("Enter the list: "))
sol=Solution()
print("Max area: ", sol.maxArea(height))
        