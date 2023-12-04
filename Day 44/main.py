class Solution():
    @staticmethod
    def threeSum(nums):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        counter=0
        for i in nums:
            counter+=1

        #combination=[]
        
        all_combinations=[]
        
        for i in range(counter):
            for j in range(i+1,counter):
                for z in range(j+1,counter):
                    if nums[i]+nums[j]+nums[z]==0:
                        combination=[]
                        combination.append(nums[i])
                        combination.append(nums[j])
                        combination.append(nums[z])
                        all_combinations.append(combination)
        
        return all_combinations 
