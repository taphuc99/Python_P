"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""
# def threeSum(self, nums: List[int]) -> List[List[int]]:

nums = [-1,0,1,2,-1,-4]
res = set()

# 1. Splits nums into three lists: negative, positive, and 0
n, p, z = [], [], []
for num in nums:
    if num < 0:
        n.append(num)
    if num > 0:
        p.append(num)
    else:
        z.append(num)

#2. Create a separate set for negatives and positives for O(1) look-up times
N, P = set(n), set(p)


