class Solution:
    def lengthOfLIS(self, nums):

        if len(nums) <= 1:
            return len(nums)

        tail = [nums[0]]

        for i in nums[1:]:

            if i > tail[-1]:
                tail.append(i)
                continue
            else:
                left = 0
                right = len(tail) - 1
                while left < right:
                    mid = (left + right) // 2
                    if tail[mid] < i:
                        left = mid + 1
                    else:
                        right = mid
                tail[right] = i

        return len(tail)
