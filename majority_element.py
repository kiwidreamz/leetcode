class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        sortedd = sorted(nums)
        counter = 0
        maxi = 0
        result = 0

        for i in range(len(sortedd)-1):
            if sortedd[i] == sortedd[i+1]:
                counter += 1
                if counter > maxi:
                    maxi = counter
                    result = sortedd[i]
            else:
                counter = 0

        return result