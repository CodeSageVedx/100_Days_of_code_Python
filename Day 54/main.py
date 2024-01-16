#Container With Most Water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r = len(height)-1
        height_tracker=0
        while l<=r:
            length = r-l
            h = min(height[l],height[r])
            if height_tracker<length*h:
                height_tracker=length*h
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
            
        return height_tracker