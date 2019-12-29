class Solution:
"""
与I的区别是可以包含重复元素
因此比较mid与righ：
  if nums[mid] == nums[right]: right = right - 1
上面是核心思想，若mid与right位置的元素相等，那么right处的元素必定不是最小值，这样可以剔除重复元素
其余与I相同
"""
    def findMin(self, nums: List[int]) -> int:
        """
        if not nums:
            return None
        
        size = len(nums)
        for i in range(size - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        
        return nums[0]
        """

        if not nums:
            return None

        size = len(nums)
        left = 0
        right = size - 1
        while left < right:
            mid = (left + right) // 2
                
            if nums[mid] == nums[right]: right = right - 1
            elif nums[mid] > nums[right]: left = mid + 1
            else: right = mid
            #print(nums[left:right+1])

        return nums[left]
