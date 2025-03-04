# Script: three_sum.py
"""
Question: 3Sum
Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` 
such that the sum of the three numbers is zero.
Avoid duplicate triplets in the output.
Example:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
"""

def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n):
        # Skip duplicate values for i.
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                # Skip duplicates for left and right.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1
    return result

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    result = three_sum(nums)
    print("Unique triplets that sum to zero:", result)
