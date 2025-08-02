# Last updated: 02/08/2025, 14:42:43
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r, max_area=0, len(height)-1, 0
        while l<r:
            min_height = min(height[l], height[r])
            area = min_height*(r-l)
            max_area = max(max_area, min_height*(r-l))
            if area > max_area:
                max_area = area
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
        return max_area