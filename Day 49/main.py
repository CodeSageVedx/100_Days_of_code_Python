# Method 1
def Binary_Search(arr, high, low, n):
    mid = (high + low) // 2
    if arr[mid] == n:
        return mid
    elif n > arr[mid]:
        return Binary_Search(arr, high, mid + 1, n)
    else:
        return Binary_Search(arr, mid, low, n)

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if target in nums:    
        return Binary_Search(nums, len(nums), 0, target)
    else:

        for i in range(len(nums)):
            element=(len(nums)-1)-i    
            if target >= nums[element]:
                return element+1

result = searchInsert([0, 1, 2, 3, 5, 7, 8], 4)
print(result)

#Method 2
class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l
        