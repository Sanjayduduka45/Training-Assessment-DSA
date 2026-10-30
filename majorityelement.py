# 1. Majority Element I
# Focus: Arrays • Frequency counting
# Given an integer array nums of size n, return its majority element. The majority element appears more than n / 2
# times. The array is guaranteed to contain a majority element.
# Example 1
# Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
# Output: 7
# Explanation: 7 appears 5 times in an array of size 9.
# Example 2
# Input: nums = [1, 1, 1, 2, 1, 2]
# Output: 1
# Explanation: 1 appears 4 times in an array of size 6.

#--> Approach 1
def majority_element(nums):
    freq={}
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for num in nums:
       if freq[num]>len(nums)//2:
           return num
nums=[2, 2, 1, 3, 2]
print(majority_element(nums))

#--> Better Approach
def majority_element(nums):
    freq={}
    n=len(nums)
    for num in nums:
        freq[num]=freq.get(num,0)+1
        if freq[num]>n//2:
            return num
nums=[2, 2, 1, 3, 2]
print(majority_element(nums))   


#My Approach is Hash Map(dictionary) approach
# Time Complexity =O(n)
# Space Complexity=O(n) -> Extra space (freq={}) is used



