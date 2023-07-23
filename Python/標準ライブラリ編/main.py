import copy

# nums = [10, 20, 30]
# nums_bak = nums.copy() # 浅いコピー
# nums[0] = 100
# print(nums) # [100, 20, 30]
# print(nums_bak) # [10, 20, 30]

nums = [10, 20, 30, [40, 50]]
nums_bak = copy.deepcopy(nums) # 深いコピー
nums[3][0] = 100
print(nums) # [10, 20, 30, [100, 50]]
print(nums_bak) # [10, 20, 30, [40, 50]]