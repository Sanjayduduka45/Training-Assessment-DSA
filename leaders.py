#  Leaders in an Array
# Focus: Arrays • Traversal from right
# Given an integer array nums, return all leaders in the array. A leader is an element strictly greater than every element
# to its right. The rightmost element is always a leader. Return leaders in the same order in which they appear in nums.
# Example 1
# Input: nums = [1, 2, 5, 3, 1, 2]
# Output: [5, 3, 2]
# Explanation: 5, 3 and 2 are greater than every element to their right.
# Example 2
# Input: nums = [-3, 4, 5, 1, -4, -5]
# Output: [5, 1, -4, -5]
# Explanation: Each listed value is strictly greater than all values to its right

def leaders(nums):
    leader=[nums[-1]]
    right=nums[-1]
    for i in range(len(nums)-1,-1,-1):
        if nums[i]>right:
            leader.append(nums[i])
            right=nums[i]
    leader.reverse()
    return leader
# nums = [1, 2, 5, 3, 1, 2]
nums = list(map(int, input().split()))
print(leaders(nums))

# My Approach is Right-to-Left Traversal

# Time Complexity is O(n)
# Space Complexity is O(n)