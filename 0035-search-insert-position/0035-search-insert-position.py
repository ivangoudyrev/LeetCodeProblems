class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums)-1

        while left <= right:
            center = (left + right) // 2
            if target == nums[center]:
                return center
            elif target < nums[center]:
                right = center - 1
            elif target > nums[center]:
                left = center + 1
        return left