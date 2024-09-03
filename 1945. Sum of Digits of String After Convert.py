class Solution:
    def getLucky(self, s: str, k: int) -> int:
        dic = {chr(i + ord('a')): str(i + 1) for i in range(26)}
        num_str = ''.join(dic[ch] for ch in s)
        while k > 0:
            num_str = str(sum(int(digit) for digit in num_str))
            k -= 1   
        return int(num_str)
