# https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0]* (len(s)+1)
        
        dp[0] = 1
        dp[1] = 0 if s[0] is 0 else 1
        
        for k in range(2,len(s)+1):
            
            if int(s[k-1:k]) > 0:
                dp[k] += dp[k-1]
            
            if 10 <= int(s[k-2:k]) <= 26:
                dp[k] += dp[k-2]
            
        return dp[len(s)]