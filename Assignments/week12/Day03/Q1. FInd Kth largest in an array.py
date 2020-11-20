## https://leetcode.com/problems/kth-largest-element-in-an-array/

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return
        heap = []
        for i in nums:
            heapq.heappush(heap,(-i,i))
        
        for j in range(k-1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)[1]
        