# Script: subarray_sum_k.py
"""
Question: Subarray Sum Equals K
Given an array of integers `nums` and an integer `k`, 
find the total number of continuous subarrays whose sum equals `k`.
Example:
    Input: nums = [1, 1, 1], k = 2
    Output: 2
"""

def subarray_sum_equals_k(nums, k):
    count = 0
    current_sum = 0
    prefix_sums = {0: 1}  # Dictionary to store frequency of prefix sums.
    
    for num in nums:
        current_sum += num
        # If (current_sum - k) is in prefix_sums, add its frequency to count.
        if current_sum - k in prefix_sums:
            count += prefix_sums[current_sum - k]
        # Update the frequency for current_sum.
        prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
    
    return count

if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    result = subarray_sum_equals_k(nums, k)
    print("Number of subarrays with sum equal to k:", result)
