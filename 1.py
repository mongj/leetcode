from typing import List

nums = [2,7,11,15]
target = 9

def twoSum(nums: List[int], target: int) -> List[int]:
    hash_table = dict()
    list_len = len(nums)
    for i in range(list_len):
        if target - nums[i] in hash_table:
            return [hash_table[target - nums[i]], i]
        else:
            hash_table[nums[i]] = i

test = twoSum(nums, target)
print(test)