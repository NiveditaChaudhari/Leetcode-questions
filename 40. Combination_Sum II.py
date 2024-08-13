from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(start:int,target:int,path:List[int]):
            if target == 0:
                arr.append(path)
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                backtracking(i+1,target-candidates[i],path+[candidates[i]])

        candidates.sort()
        arr=[]
        backtracking(0,target,[])
        return arr
    
nums=eval(input("Enter numbers separated by spaces: ")) #[10,1,2,7,6,1,5]
target=int(input("Target Sum: ")) #8
sol = Solution()
print("Index are: ",sol.combinationSum2(nums,target))

