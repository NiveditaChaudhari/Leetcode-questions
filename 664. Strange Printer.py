class Solution:
    def strangePrinter(self, s: str) -> int:
        n=len(s)
        memo={}
        def solve(l,r):
            if l>r:
                return 0
            if (l,r) in memo:
                return memo[(l,r)]
            
            while r>l and s[r] == s[l]:
                r-=1
            res=1+solve(l+1,r)

            for j in range(l+1,r+1):
                if s[j]==s[l]:
                    res=min(res,solve(l,j-1)+solve(j+1,r))
            memo[(l,r)] = res
            return res
        return solve(0,n-1)

s=input("Enter the string: ")
sol=Solution()
print("Minimal solution: ", sol.strangePrinter(s))