# Script: decode_ways.py
"""
Question: Decode Ways
A message containing letters from A-Z can be encoded to numbers using the mapping 
`A -> 1, B -> 2, …, Z -> 26`.
Given a non-empty string containing only digits, determine the total number of ways 
to decode it.
Example:
    Input: s = "12"
    Output: 2   # ("AB" or "L")
"""

def num_decodings(s):
    if not s or s[0] == "0":
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string has one way to decode.
    dp[1] = 1  # A non-zero single digit can only be decoded one way.
    
    for i in range(2, n + 1):
        # One-digit decode (if the current digit is not '0').
        if s[i-1] != "0":
            dp[i] += dp[i-1]
        # Two-digit decode (check if the two-digit number is between 10 and 26).
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]

if __name__ == "__main__":
    s = "12"
    result = num_decodings(s)
    print("Number of ways to decode the string:", result)
