# Reverse Pairs
# Focus: Arrays • Merge sort
# Given an integer array nums, count the pairs of indices (i, j) satisfying 0 ≤ i < j < nums.length and nums[i] > 2 ×
# nums[j].
# Example 1
# Input: nums = [6, 4, 1, 2, 7]
# Output: 3
# Explanation: The reverse pairs are (0,2), (0,3) and (1,2).
# Example 2
# Input: nums = [5, 4, 4, 3, 3]
# Output: 0
# Explanation: No pair satisfies nums[i] > 2 × nums[j].

# Brute Force Approach 
# TC is O(n*n)
# SC is O(n)

def revpairs(nums):
    n=len(nums)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>2*nums[j]:
                count+=1
    return count
# nums = [6, 4, 1, 2, 7]
nums=list(map(int,input().split()))
print(revpairs(nums))


def revpairscount(nums):
    if len(nums)<=1:
        return 0
    mid=len(nums)//2
    left=nums[:mid]
    right=nums[mid:]
    revpairscount(left)
    revpairscount(right)
    i=j=0
    count=0
    while i<len(left) and j<len(right):
        if left[i]>2*right[j]:
            count+=1
            i+=1
        else:
            count+=1
            j+=1
    while i<len(left):
        count+=1
        i+=1
    while j<len(right):
        count+=1
        j+=1
        