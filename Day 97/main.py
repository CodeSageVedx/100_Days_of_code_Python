# Search in Rotated Sorted Array II
class Solution(object):
    def search(self, nums, target):
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True

            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False