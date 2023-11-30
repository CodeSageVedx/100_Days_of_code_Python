class Solution():
    @staticmethod
    def findMedianSortedArrays( nums1, nums2):
        merged_array=[]
        for i in range(len(nums1)):
            merged_array.append(nums1[i])
        for i in range(len(nums2)):
            merged_array.append(nums2[i])
        merged_array.sort()
        merged_len=len(merged_array)
        if merged_len%2 == 0:
            midpoint = merged_len // 2
            median = float(merged_array[midpoint] + merged_array[midpoint - 1]) / 2
        else:
            midpoint = merged_len // 2
            median = merged_array[midpoint]
        return median