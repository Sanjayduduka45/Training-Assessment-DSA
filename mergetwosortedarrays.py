# erge Two Sorted Arrays Without Extra Space
# Focus: Arrays • Two pointers
# Given two sorted integer arrays nums1 and nums2, merge them into sorted order in-place. nums1 has length m + n:
# its first m elements are valid values and its remaining n positions are placeholders. nums2 has length n. Store the final
# merged array in nums1.
# Example 1
# Input: nums1 = [-5, -2, 4, 5, 0, 0, 0]; nums2 = [-3, 1, 8]
# Output: [-5, -3, -2, 1, 4, 5, 8]
# Explanation: The final sorted array is stored in nums1.
# Example 2
# Input: nums1 = [0, 2, 7, 8, 0, 0, 0]; nums2 = [-7, -3, -1]
# Output: [-7, -3, -1, 0, 2, 7, 8]
# Explanation: Merge the valid elements from both arrays.


def mergetwosortedarrays(nums1,nums2,m,n):
    left=m-1
    right=n-1
    pos=len(nums1)-1
    while left>=0 and right>=0:
        if nums1[left]>=nums2[right]:
            nums1[pos]=nums1[left]
            left-=1
        else:
            nums1[pos]=nums2[right]
            right-=1
        pos-=1
    while right>=0:
        nums1[pos]=nums2[right]
        right-=1
        pos-=1
    return nums1
# nums1=[1,2,3,0,0,0]
nums1=list(map(int,input().split()))
m = 3
nums2=list(map(int,input().split()))
# nums2 = [2,5,6]
n = 3
print(mergetwosortedarrays(nums1,nums2,m,n))

# My Approach is Two-Pointers
# Time Complexity is O(n)
# Space Complexity is O(1)
