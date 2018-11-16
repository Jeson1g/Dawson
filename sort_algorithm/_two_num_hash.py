def twoSum(nums, target):
    """两数之和 -> hash
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_dict = {}
    for nums_ndx, num in enumerate(nums):
        if target - num in nums_dict and nums_dict[target - num] != nums_ndx:
            return nums_dict[target - num], nums_ndx
        nums_dict[num] = nums_ndx