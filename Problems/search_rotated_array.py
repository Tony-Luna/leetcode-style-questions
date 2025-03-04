# Script: search_rotated_array.py
"""
Question: Search in Rotated Sorted Array
Given a rotated sorted array `nums` and a target value, 
return the index of the target if found; otherwise, return -1.
The algorithm should have O(log n) runtime complexity.
Example:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
"""

def search_rotated_array(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        
        # Check if mid is the target
        if nums[mid] == target:
            return mid
        
        # Determine which half is sorted
        if nums[left] <= nums[mid]:
            # Left half is sorted.
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half is sorted.
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    
    index = search_rotated_array(nums, target)
    print("Index of target:", index)
