class Solution:
    def findComplement(self, num: int) -> int:
        return num^(1<<num.bit_length())-1
        
        # OR
        # num=bin(num)
        # num=list(num)
        # for i in range(2,len(num)):
        #     if (num[i])=='0':
        #         num[i]='1'
        #     elif (num[i])=='1':
        #         num[i]='0'
        # ans=''.join(num)
        # return int(ans,2)

num=int(input("Enter a number: "))
sol=Solution()
print("Ans: ",sol.findComplement(num))