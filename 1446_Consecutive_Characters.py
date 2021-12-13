class Solution:
    def maxPower(self, s: str) -> int:
       
        count = 1
        prev = s[0]
        ans = 1
        for i in range(1,len(s)):
            if s[i]==prev:
                count+=1
            else:
                count = 1
            
            prev = s[i]
            ans = max(ans,count)
        
        return ans
            