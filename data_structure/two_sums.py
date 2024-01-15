# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

arr = [7,11,15,2,20]

def two_sum(nums, target):
    map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in map:
            return [map[diff], i]
        else:
            map[num] = i

print(two_sum(arr, 9))



# brute force way O(n^2)
# nested for loops -> first loop starts at index 0 and second loop starts at index second

def two_sums(nums, target):
    for i in range(len(nums)):
        for k in range(len(nums) - 1):
            if nums[i] + nums[k] == target:
                return [i, k]


print(two_sums([1,2,7,3,4], 9))