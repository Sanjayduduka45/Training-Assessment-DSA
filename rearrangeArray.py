# Rearrange Array Elements by Sign
# Focus: Arrays • Two pointers / indexing
# Given an even-length array with an equal number of positive and negative integers, rearrange it so that consecutive
# elements have opposite signs, the result starts with a positive integer, and the relative order of positive values and of
# negative values is preserved.
# Example 1
# Input: nums = [2, 4, 5, -1, -3, -4]
# Output: [2, -1, 4, -3, 5, -4]
# Explanation: Positive and negative values each keep their original relative order.
# Example 2
# Input: nums = [1, -1, -3, -4, 2, 3]
# Output: [1, -1, 2, -3, 3, -4]
# Explanation: The output alternates signs and begins with a positive value.

# --> My Approach is Fixed Index Placement
def rearrangeArray(nums):
    n=len(nums)
    res=[0]*n
    pos=0
    neg=1
    for num in nums:
        if num>0:
            res[pos]=num
            pos+=2
        else:
            res[neg]=num
            neg+=2
    return res

nums=list(map(int,input().split()))
print(rearrangeArray(nums))