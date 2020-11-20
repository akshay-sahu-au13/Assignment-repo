## https://leetcode.com/problems/longest-increasing-subsequence/submissions/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        L = len(nums)
        List = []
        
        for i in range(L):
            if len(List) ==0 or List[len(List)-1]<nums[i]:
                List.append(nums[i])
            else:
                left,right = 0, len(List)
                while left < right:
                    mid = (left+right)//2
                    if nums[i] > List[mid]:
                        left = mid+1
                    elif nums[i] < List[mid]:
                        right = mid
                    else:
                        right = mid
                List[left] = nums[i]
        
        return len(List)