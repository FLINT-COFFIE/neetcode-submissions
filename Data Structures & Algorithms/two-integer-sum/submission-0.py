class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values_and_index = {}

        for index, number in enumerate(nums):
            difference = target - number
            if difference in values_and_index:
                return [values_and_index[difference], index]

            values_and_index[number] = index