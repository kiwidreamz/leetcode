class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(l):
            for j in range(1, l):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]