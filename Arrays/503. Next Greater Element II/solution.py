class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        empty_list = [-1] * len(nums)
        for i in range(len(nums)):
            for j in range(i + 1, i + len(nums)):
                index = j % len(nums)
                if nums[index] > nums[i]:
                    empty_list[i] = nums[index]
                    break
        return empty_list