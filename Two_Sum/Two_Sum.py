class Solution(object):
    def twoSum(self, nums, target):
        """
		Brute Force

        Time Complexity | Space Complexity |  Run Time
           O(n^2)           O(1)                4944ms 

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index_i, i in enumerate(nums):
            for index_j, j in enumerate(nums[index_i+1:]):
                if j + i == target:
                    return [index_i + 1, index_j + index_i + 2] 

    def twoSum(self, nums, target):
    """
    Hash Table

    Time Complexity | Space Complexity |  Run Time
       O(n)           O(n)                 40ms

    Create a hash table, the difference between target and the first element(the num
    -ber we need) stores as key, and index of first element as value.
    """
    ht = dict()
    for index_i, i in enumerate(nums):
	if i in ht: # if this number is needed
	    return [ht[i] + 1, index_i + 1]	
        ht[target - i] = index_i

# Consideration
# 20151124
# What if the nums is like [2, 2, 4, 5] and the target is 6,
# the hash table method will return [2, 3], but I think the 
# right result is [1, 3]
def twoSum(self, nums, target):
    ht = dict()
    for index_i, i in enumerate(nums):
        if i in ht:
            return [ht[i][0] + 1, index_i + 1]
        else:
            if target - i in ht and ht[target - i] is not None:
                # or we can just abondon it
                ht[target - i].append(index_i)
            else:
                ht[target - i] = [index_i]
