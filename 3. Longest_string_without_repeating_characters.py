class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return
        map={}
        max_count=start=0
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start=map[s[i]]+1
            else:
                max_count = max(max_count,i-start+1)
            map[s[i]]=i
            print(map)
        return max_count

    
string=input("String input: ")
sol = Solution()
print("Index are: ",sol.lengthOfLongestSubstring(string))