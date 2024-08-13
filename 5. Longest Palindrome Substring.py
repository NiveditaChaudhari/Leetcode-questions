class Solution:
    def longestPalindrome(self, s: str) -> str:
            start=0
            dic={}
            n=len(s)
            max_len=1
            def long_pal(i,j):
                  nonlocal start, max_len
                  while i>=0 and j<n and s[i]==s[j]:
                        curr=j-i+1
                        if curr > max_len:
                              start=i
                              max_len = curr
                        i-=1
                        j+=1
            for x in range(n):
                  long_pal(x,x)
                  long_pal(x,x+1)
            return s[start:start+max_len]


s=input("Input the string: ")
sol=Solution()
print(sol.longestPalindrome(s))