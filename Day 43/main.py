class Solution(object):
    def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        counter=0
        for i in nums:
            counter+=1

        combination=[]

        for i in range(counter):
            for j in range(i+1,counter):
                if nums[i]+nums[j]==target:
                    combination.append(i)
                    combination.append(j)
        
                    return combination