"""
二分法的其他应用--寻找旋转有序列表中的旋转点（最小值），如[4,5,6,7,0,1,3]中的0
假设不含有重复元素

当left = right说明此时该元素即为最小值
由于旋转有序列表中，每一段都是单调递增的，且第二段要比第一段小

因此若查找位置的值比nums[right]大，那么它肯定是属于第一段的,那么旋转点，即最小元素必定在查找位置的右边，故left = mid + 1，

反之，则属于第二段，故旋转点必定在此元素的左边，
注意这里的左边依然包含该元素，由于不知道该查找元素是否是第二段的起点，因此更新right = mid
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:

        if not nums:
            return None

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
