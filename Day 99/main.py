class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
      rightSmall = []
      right = []
      leftSmall = []
      left = []
      for i in range(len(heights)):
        # print(len(leftSmall)-1 , heights , leftSmall , left)
        if len(leftSmall) == 0:
            left.append(-1)
            leftSmall.append(i)
            next
        elif heights[leftSmall[len(leftSmall)-1]] < heights[i]:
          left.append(leftSmall[len(leftSmall)-1]+1)
          leftSmall.append(i)
        else:
          while len(leftSmall) != 0 and heights[leftSmall[len(leftSmall)-1]] >= heights[i]:
            leftSmall.pop()
          if len(leftSmall) == 0:
            left.append(-1)
            leftSmall.append(i)
          elif heights[leftSmall[len(leftSmall)-1]] < heights[i]:
            left.append(leftSmall[len(leftSmall)-1]+1)
            leftSmall.append(i)
      
      for i in range(len(heights)-1 , -1, -1):
        if len(rightSmall) == 0:
          right.append(-1)
          rightSmall.append(i)
        elif heights[rightSmall[len(rightSmall)-1]] < heights[i]:
          right.append(rightSmall[len(rightSmall)-1]-1)
          rightSmall.append(i)
        else:
          while len(rightSmall) != 0 and heights[rightSmall[len(rightSmall)-1]] >= heights[i]:
            rightSmall.pop()
          if len(rightSmall) == 0:
            right.append(-1)
          elif heights[rightSmall[len(rightSmall)-1]] < heights[i]:
            right.append(rightSmall[len(rightSmall)-1]-1)
          rightSmall.append(i)

      maxa = 0
      right.reverse()
      
      for i in range(len(heights)):
        if left[i] == -1:
          left[i] = 0
      
        if right[i] == -1 :
          right[i] = len(heights)-1
        
        maxa = max(maxa , (heights[i]*(right[i] - left[i] +1)))
      return maxa
  