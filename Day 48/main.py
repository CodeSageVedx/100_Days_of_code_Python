class Solution:
    def searchRange(self, nums, target):
        n=len(nums)
        left=0
        right=n-1
        if target in nums:
            for i in range(0,n):
                if nums[left]==nums[right]:
                    return [left,right] 
                elif nums[left]<target:
                    left+=1
                else:
                    right-=1
        else:
            return [-1,-1]                           