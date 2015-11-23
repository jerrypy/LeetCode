class Solution(object):
    def twoSum(self, nums, target):
        """
        O(n^2)
	"""
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_i, i in enumerate(nums):
            for index_j, j in enumerate(nums[index_i+1:]):
                if j + i == target:
                    return [index_i + 1, index_j + index_i + 2] 
