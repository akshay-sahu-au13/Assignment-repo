https://practice.geeksforgeeks.org/problems/coin-change2448/1

class Solution:
    def count(self, S, m, n): 
        # code here 
        dp = [0]*(n+1)
        dp[0] = 1
        for cents in S:
            for j in range(cents,len(dp)):
                dp[j] = dp[j]+dp[j-cents]
        return dp[n]


