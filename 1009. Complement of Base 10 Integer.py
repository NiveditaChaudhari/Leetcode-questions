class Solution:
    def bitwiseComplement(self, num: int) -> int:
        if num==0:
            return 1
        return num^(1<<num.bit_length())-1
    
num=int(input("Enter the number: "))
sol=Solution()
print("Ans: ", sol.bitwiseComplement(num))