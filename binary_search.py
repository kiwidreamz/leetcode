class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) -1
        low = 0
        while low <= high:
            current = low + (high - low) // 2
            if nums[current] == target:
                return current
            elif nums[current] < target:
                low = current + 1
            else:
                high = current - 1
        return -1