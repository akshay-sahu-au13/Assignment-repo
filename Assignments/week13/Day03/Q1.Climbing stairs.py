## https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*n
        return self.Climb_Stairs(0,n,dp)
    
    def Climb_Stairs(self,i,n,dp):
        
        if i > n:
            return 0
        if i == n:
            return 1
        
        if dp[i] > 0:
            return dp[i]
        
        dp[i] = self.Climb_Stairs(i+1,n,dp) + self.Climb_Stairs(i+2,n,dp)
        
        return dp[i]
            
            