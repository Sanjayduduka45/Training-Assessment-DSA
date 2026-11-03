#  Count Inversions
# Focus: Arrays • Merge sort
# Given an integer array nums, return its inversion count. A pair of indices (i, j) is an inversion when i < j and nums[i] >
# nums[j]. A sorted array has zero inversions.
# Example 1
# Input: nums = [2, 3, 7, 1, 3, 5]
# Output: 5
# Explanation: The inversions are (2,1), (3,1), (7,1), (7,3) and (7,5), using their original index positions.
# Example 2
# Input: nums = [-10, -5, 6, 11, 15, 17]
# Output: 0
# Explanation: The array is already sorted, so it has no inversions.

#--> My Approach is Merge Sort

# def merge_sort(nums):
#     n=len(nums)
#     if n<=1:
#         return nums,0
#     mid=len(nums)//2
#     left,left_count= merge_sort(nums[:mid])
#     right,right_count=merge_sort(nums[mid:])
#     i=j=count=0
#     res=[]
#     while i < len(left) and j < len(right):
#         if left[i]<=right[j]:
#             res.append(left[i])
#             i+=1
#         else:
#             res.append(right[j])
#             j+=1
#             count+=len(left)-i
#     res.extend(left[i:])
#     res.extend(right[j:])
#     return res, left_count+right_count+count
# nums=list(map(int,input().split()))
# print(merge_sort(nums))



# --> Count Inversions

def inversionCount(arr):
    def merge_sort(nums):
        if len(nums)<=1:
            return nums,0
        mid=len(nums)//2
        left,left_count=merge_sort(nums[:mid])
        right,right_count=merge_sort(nums[mid:])
        i=j=count=0
        res=[]
        while i < len(left) and j < len(right):
            if left[i]<=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
                count+=len(left)-i
        res.extend(left[i:])
        res.extend(right[j:])
        return res, left_count + right_count + count
    sorted_arr , total_count = merge_sort(arr)
    return total_count
nums=list(map(int,input().split()))
print(inversionCount(nums))