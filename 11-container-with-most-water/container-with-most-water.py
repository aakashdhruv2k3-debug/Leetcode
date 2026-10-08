class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        max_water = 0

        while left < right:
            currentHeight = min(height[left], height[right])
            currentWidth = right - left
            current_water = currentHeight * currentWidth

            if(current_water>max_water):
                max_water = current_water
            
            if(height[left]<height[right]):
                left+=1
            else:
                right-=1
        return max_water
        