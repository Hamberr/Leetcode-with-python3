class Solution:

"""
envelopes.sort(key=lambda t:(t[0],-t[1]))实现二维列表第一维升序排列，第二维降序排列（第一位元素相同的情况下）
这样就将套娃问题转化为求第二维的最长上升子序列问题
因此之所以将第二维倒序，就是避免将统一宽度的信封多选
"""

    def lengthOfLIS(self, nums):

        if len(nums) < 2:
            return len(nums)

        tail = [nums[0]]
        for num in nums:
            if num > tail[-1]:
                tail.append(num)
                continue           
            left = 0
            right = len(tail) - 1
            while left < right:
                mid = (left + right) // 2
                if num > tail[mid]:
                    left = mid + 1
                else:
                    right = mid
            tail[right] = num

        return len(tail)


    def maxEnvelopes(self, envelopes):

        if len(envelopes) <= 1:
            return len(envelopes)

        envelopes.sort(key=lambda t:(t[0],-t[1]))
        list_height = [envelope[1] for envelope in envelopes]
        return self.lengthOfLIS(list_height)
