# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true


# hashmap 
# create an empty hashmap 
# if value exist in hashmap then print true 
# if not then add the value to hashmap 

def contains_duplicate(nums):
    hash_map = {}

    for i in nums:
        if i in hash_map:
            return True
        else: 
            hash_map[i] = i 
    return False

print(contains_duplicate([1,2,3,4]))
