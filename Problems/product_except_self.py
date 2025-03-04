# Script: product_except_self.py
"""
Question: Product of Array Except Self
Given an integer array `nums`, return an array `answer` 
such that `answer[i]` is equal to the product of all the 
elements of `nums` except `nums[i]`. 
Solve without using division and in O(n) time.
Example:
    Input: nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]
"""

def product_array_except_self(nums):
    length = len(nums)
    # Initialize the answer array with 1's
    answer = [1] * length

    # Calculate left products
    left = 1
    for i in range(length):
        answer[i] = left
        left *= nums[i]

    # Multiply with right products
    right = 1
    for i in range(length - 1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer

if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    answer = product_array_except_self(nums)
    print(answer)
