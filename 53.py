from typing import List

nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    cur_sum = nums[0]
    nums_len = len(nums)
    for i in range(1, nums_len):
        cur_sum = max(nums[i], cur_sum + nums[i])
        max_sum = max(cur_sum, max_sum)
    return max_sum

test = maxSubArray(nums)
print(test)