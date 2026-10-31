# Kadane's Algorithm — Maximum Subarray Sum
# Focus: Arrays • Dynamic programming
# Given an integer array nums, find the non-empty contiguous subarray with the largest sum and return that sum.
# Example 1
# Input: nums = [2, 3, 5, -2, 7, -4]
# Output: 15
# Explanation: The subarray [2, 3, 5, -2, 7] has sum 15.
# Example 2
# Input: nums = [-2, -3, -7, -2, -10, -4]
# Output: -2
# Explanation: The maximum sum is the largest individual element, -2.

def maxsubarraysum(nums):
    curr_sum=nums[0]
    max_sum=curr_sum
    n=len(nums)
    for i in range(1,n):
        curr_sum=max(nums[i],curr_sum+nums[i])
        max_sum=max(max_sum,curr_sum)
    return max_sum
#nums=[2, 3, 5, -2, 7, -4]
nums = list(map(int, input().split()))
print(maxsubarraysum(nums))

# My Approach is Kadens Algorithm

#Time Complexity is O(n)
#Space Complexity is O(1) -> No extra space is used