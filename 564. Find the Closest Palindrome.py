class Solution:
    def nearestPalindromic(self, n: str)->str: 
        l=len(n)
        candidates =set()
        if n=='1':
            return '0'
        
        prefix=n[:(l+1)//2]
        prefix_number=int(prefix)

        for i in [-1,0,1]:
            new_prefix = str(prefix_number+i)
            if l%2==0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate= new_prefix + new_prefix[:-1][::-1]
            candidates.add(candidate)
        
        candidates.add(str(10**(l-1)-1))
        candidates.add(str(10**l+1))

        candidates.discard(n)
        closest_palindrome = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))
        
        return closest_palindrome
            

n=input("Enter the number: ")
sol=Solution()
print("Ans: ", sol.nearestPalindromic(n))