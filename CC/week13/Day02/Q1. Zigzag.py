## https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s 
        n = len(s)
        rows = 2*numRows - 2
        List = []
        for i in range(numRows):
            for j in range(i, n, rows):
                List.append(s[j])
                if i != numRows-1 and i != 0 and j+rows-2*i < n:
                    List.append(s[j+rows-2*i])             
        Zigzag = ''.join(List)
        return Zigzag
        
            
            
        