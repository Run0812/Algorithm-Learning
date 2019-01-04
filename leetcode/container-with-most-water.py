def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left = 0
    right = len(height) - 1
    area = 0
    while left < right:
        area = max(area, (right - left) * min(height[left], height[right]))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))