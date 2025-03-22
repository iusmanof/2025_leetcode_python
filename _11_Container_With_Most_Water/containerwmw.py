class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result_area = 0
        l, r = 0, len(height) - 1
        print(l)
        print(r)
        while l < r:
            y = min(height[l], height[r])
            x = r - l
            area = x * y
            result_area = max(result_area, area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1
        return result_area